import sympy

def right_truncatable_prime(n):
    return all((sympy.isprime(int(n[i:j])) for i in range(len(n)) for j in range(i + 1, len(n) + 1)))

def all_right_truncatable_prime(numbers):
    primes = []
    x = numbers[50]
    for i in range(2, x):
        if sympy.isprime(i) and right_truncatable_prime(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)