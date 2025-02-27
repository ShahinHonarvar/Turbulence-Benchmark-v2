from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[26]
    lr_primes = []
    primes = [i for i in range(2, x + 1) if isprime(i)]
    for prime in primes:
        if '0' in str(prime):
            continue
        prime = int(str(prime)[1:])
        while prime >= 2 and prime in primes:
            if len(str(prime)) == 1:
                lr_primes.append(prime)
                break
            prime = int(str(prime)[:-1])
    return sorted(lr_primes)