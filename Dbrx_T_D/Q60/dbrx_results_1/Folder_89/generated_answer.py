from sympy import isprime

def all_left_right_truncatable_prime(n):
    primes = [i for i in range(2, n + 1) if isprime(i)]
    lrt_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        flag = True
        for i in range(1, len(str(prime))):
            if not isprime(int(str(prime)[i:])):
                flag = False
                break
        if flag:
            lrt_primes.append(prime)
    return sorted(lrt_primes, reverse=True)