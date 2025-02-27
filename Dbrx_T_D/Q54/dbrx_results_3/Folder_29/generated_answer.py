from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    primes = [i for i in range(1, x) if isprime(i)]
    trunc_primes = []
    for prime in primes:
        while prime > 0:
            if isprime(prime):
                trunc_primes.append(prime)
            prime //= 10
    return sorted(list(set(trunc_primes)), reverse=True)