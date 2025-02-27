from sympy import isprime

def all_right_truncatable_prime(tp):
    x = tp[30]
    primes = [i for i in range(2, x) if isprime(i)]
    right_truncatable_primes = []
    for i in primes:
        num = i
        while num > 9:
            num //= 10
        if isprime(num) and num in primes:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)