def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and left_truncatable_prime(int(str(n)[1:]))

def all_left_truncatable_prime(t):
    x = t[61]
    result = []
    for i in range(1, x):
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result)