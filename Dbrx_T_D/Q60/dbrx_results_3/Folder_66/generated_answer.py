from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[25]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatable_primes = []

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    for prime in primes:
        if is_left_truncatable_prime(prime) and is_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)