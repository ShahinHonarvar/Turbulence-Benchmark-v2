from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[69]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    lr_trunc_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        flag = True
        while len(str(prime)) > 1:
            prime = int(str(prime)[1:])
            if not isprime(prime):
                flag = False
                break
        if flag:
            lr_trunc_primes.append(prime)
    return sorted(lr_trunc_primes, reverse=True)