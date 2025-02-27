from sympy import isprime, primerange

def all_right_truncatable_prime(numbers):
    x = numbers[767]
    right_truncatable_primes = []
    for p in primerange(1, x):
        if all((isprime(int(str(p)[:i])) for i in range(1, len(str(p)) + 1))):
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes, reverse=True)