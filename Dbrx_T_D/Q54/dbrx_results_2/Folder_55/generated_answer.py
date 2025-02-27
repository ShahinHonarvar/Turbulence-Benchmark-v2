from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    all_right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    all_right_truncatable_primes.sort(reverse=True)
    return all_right_truncatable_primes