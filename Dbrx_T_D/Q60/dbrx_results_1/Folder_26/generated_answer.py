from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_truncatable_prime(num):
        if num < 10:
            return isprime(num)
        while num % 10 == 0 or num % 10 == num // 10:
            num //= 10
        return isprime(num)

    def is_right_truncatable_prime(num):
        while num >= 10:
            if not isprime(num % 10):
                return False
            num //= 10
        return isprime(num)
    primes = [i for i in range(10, n + 1) if is_left_truncatable_prime(i) and is_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)