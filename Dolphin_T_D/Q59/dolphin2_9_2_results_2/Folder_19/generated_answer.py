import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    left_truncatable_primes = []
    for prime in sympy.primerange(2, x):
        if sympy.isprime(int(str(prime)[1:])) and int(str(prime)[1:]):
            temp = int(str(prime)[1:])
            while temp:
                if not sympy.isprime(temp):
                    break
                temp = int(str(temp)[1:])
            else:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)