from functools import cmp_to_key

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if is_prime(i):
            digit = i % 10
            while digit > 0:
                i //= 10
                if is_prime(i):
                    digit = i % 10
                else:
                    break
            if digit == 0:
                result.append(i)
    return sorted(result, key=cmp_to_key(lambda a, b: b - a))