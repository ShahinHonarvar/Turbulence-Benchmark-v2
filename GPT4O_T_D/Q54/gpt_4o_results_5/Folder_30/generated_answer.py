from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) < 38:
        return []
    x = numbers[37]

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not isprime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    right_truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes, reverse=True)