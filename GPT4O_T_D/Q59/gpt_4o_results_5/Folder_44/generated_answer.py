from sympy import isprime

def all_left_truncatable_prime(numbers):
    if len(numbers) < 40:
        return []
    x = numbers[39]
    primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all((isprime(int(str_n[i:])) for i in range(len(str_n))))
    for num in range(2, x):
        if isprime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return primes