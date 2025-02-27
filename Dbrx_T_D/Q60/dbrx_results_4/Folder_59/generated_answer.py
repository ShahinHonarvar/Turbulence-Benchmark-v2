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

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if '0' in str(n):
        return False
    for i in range(len(str(n)) // 2 + 1):
        if not is_prime(n // 10 ** i % 10 ** (len(str(n)) // 2 + 1 - i)):
            return False
    return True

def all_left_right_truncatable_prime(r):
    x = sorted(r)[84]
    return sorted(filter(is_left_right_truncatable_prime, range(11, x + 1)))[::-1]