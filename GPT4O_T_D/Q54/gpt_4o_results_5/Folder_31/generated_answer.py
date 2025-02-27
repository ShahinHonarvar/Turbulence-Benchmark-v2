from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 50:
        return []
    x = numbers[50]

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[:-1]
            if not isprime(int(str_n)):
                return False
        return True
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes, reverse=True)