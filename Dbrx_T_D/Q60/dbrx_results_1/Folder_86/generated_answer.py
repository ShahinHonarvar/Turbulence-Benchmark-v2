from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n % (10 * (n // 10))
        return True
    left_and_right_truncatable_primes = []
    x = min(tup[126], 10)
    for num in range(11, x + 1):
        if isprime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_and_right_truncatable_primes.append(num)
    return left_and_right_truncatable_primes[::-1]