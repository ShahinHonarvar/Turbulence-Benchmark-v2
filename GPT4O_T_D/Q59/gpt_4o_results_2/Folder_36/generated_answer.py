from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[992]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes