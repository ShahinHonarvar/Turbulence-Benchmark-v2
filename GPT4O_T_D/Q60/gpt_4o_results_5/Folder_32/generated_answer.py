from sympy import isprime

def truncatable_primes(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not (isprime(int(str_n[i:])) and isprime(int(str_n[:i + 1]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 42:
        return []
    x = numbers[42]
    result = []
    for i in range(10, x + 1):
        if '0' not in str(i) and isprime(i) and truncatable_primes(i):
            result.append(i)
    return result