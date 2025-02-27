def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    if n < 10:
        return [k for k in range(2, n) if is_prime(k)]
    result = []
    for k in range(10, n):
        if is_prime(k) and is_prime(int(str(k)[1:])):
            result.append(k)
    return result

def all_left_truncatable_prime(t):
    x = t[24]
    return sorted(left_truncatable_prime(x))