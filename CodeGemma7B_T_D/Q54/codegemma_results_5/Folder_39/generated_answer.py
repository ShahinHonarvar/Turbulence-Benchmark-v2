from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num = int(str(num)[:-1])
            else:
                result.append(i)
    return sorted(result, reverse=True)