from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 49:
        return []
    x = numbers[49]
    truncatable_primes = []

    def is_right_truncatable_prime(num):
        if not isprime(num):
            return False
        num_str = str(num)
        while len(num_str) > 1:
            num_str = num_str[:-1]
            if not isprime(int(num_str)):
                return False
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)