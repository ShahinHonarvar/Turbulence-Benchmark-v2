from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[803]
    lr_truncatable_primes = []

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n % (10 * (n // 10 + 1))
        return True

    def is_both_truncatable(n):
        return is_left_truncatable(n) and is_right_truncatable(n)
    for num in range(1, x + 1):
        if is_both_truncatable(num):
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes)