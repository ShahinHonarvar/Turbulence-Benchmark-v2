from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = [i for i in range(2, x) if isprime(i)]
    right_truncatable_primes = []
    for prime in primes:
        while prime > 0:
            if isprime(prime):
                right_truncatable_primes.append(prime)
            prime //= 10
    return sorted(list(set(right_truncatable_primes)), reverse=True)