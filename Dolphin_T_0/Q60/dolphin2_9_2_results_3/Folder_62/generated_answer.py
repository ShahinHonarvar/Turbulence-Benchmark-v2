import sympy

def is_truncatable_prime(n):
    if sympy.isprime(n) == False:
        return False
    if n < 10:
        return True
    str_n = str(n)
    for i in range(1, len(str_n)):
        if sympy.isprime(int(str_n[i:])) == False or sympy.isprime(int(str_n[:i])) == False:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for n in range(2, numbers + 1):
        if is_truncatable_prime(n) == True:
            truncatable_primes.append(n)
    return truncatable_primes