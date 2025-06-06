def all_right_truncatable_prime(a):
    x = a[24]
    result = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n > 0:
                if not is_prime(n):
                    break
                result.append(i)
                n //= 10
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True