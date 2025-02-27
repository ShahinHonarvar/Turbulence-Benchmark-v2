from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        str_n = str(n)
        return '0' not in str_n and all((isprime(int(str_n[i:])) for i in range(len(str_n))))
    x = numbers[87]
    left_truncatable_primes = [n for n in range(2, x) if isprime(n) and is_left_truncatable(n)]
    return sorted(left_truncatable_primes)