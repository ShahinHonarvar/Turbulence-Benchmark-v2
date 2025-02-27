from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    x = numbers[630] if len(numbers) > 630 else 0
    truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)