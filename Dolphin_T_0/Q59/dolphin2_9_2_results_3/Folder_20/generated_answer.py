from sympy import isprime

def all_left_truncatable_prime(n):
    x = n[100]
    primes = [i for i in range(2, x) if isprime(i)]
    return sorted([i for i in primes if all((isprime(i // 10 ** j) for j in range(1, len(str(i))) if i // 10 ** j != 1))], reverse=True)