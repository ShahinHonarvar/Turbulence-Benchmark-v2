from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 69 or not numbers[69] > 0:
        return []

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not isprime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    x = numbers[69]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)