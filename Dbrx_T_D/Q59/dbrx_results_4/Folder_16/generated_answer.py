from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[792]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    for num in range(1, x):
        if isprime(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)