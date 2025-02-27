import sympy

def is_right_truncatable_prime(n):
    digit = 1
    while digit <= len(str(n)):
        if sympy.isprime(int(str(n)[-digit:])):
            if digit == len(str(n)):
                return True
            else:
                digit += 1
        else:
            return False

def all_right_truncatable_prime(n):
    right_truncatable_primes = {}
    for i in range(2, n):
        if sympy.isprime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes[i] = True
    return sorted(list(right_truncatable_primes.keys()), reverse=True)