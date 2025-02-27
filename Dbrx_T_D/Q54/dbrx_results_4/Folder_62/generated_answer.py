from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[70]
    prime_numbers = [i for i in range(2, x) if isprime(i)]
    right_truncatable_primes = []
    for prime in prime_numbers:
        while prime > 0:
            if isprime(prime):
                right_truncatable_primes.append(prime)
            prime = int(str(prime)[:-1])
    return sorted(list(set(right_truncatable_primes)))