def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0 or n != int(str(n)[1:-1]):
        return False
    return is_left_right_truncatable_prime(int(str(n)[1:-1]))

def all_left_right_truncatable_prime(args):
    x = args[65]
    primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(primes, reverse=True) if primes else []