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

def right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and right_truncatable_prime(n // 10)

def all_right_truncatable_prime(t):
    x = t[758]
    primes = [i for i in range(2, x) if right_truncatable_prime(i)]
    return sorted(primes)