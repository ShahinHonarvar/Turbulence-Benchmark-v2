import sympy

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(len(s)):
        if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 20:
        return []
    x = numbers[20]
    primes = []
    for num in range(11, x + 1):
        if sympy.isprime(num) and is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)