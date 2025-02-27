from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    x = numbers_tuple[466]
    left_truncatable_primes = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)