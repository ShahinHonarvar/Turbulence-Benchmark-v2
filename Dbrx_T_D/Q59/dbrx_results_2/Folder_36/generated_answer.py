from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[992]

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    primes = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(primes)