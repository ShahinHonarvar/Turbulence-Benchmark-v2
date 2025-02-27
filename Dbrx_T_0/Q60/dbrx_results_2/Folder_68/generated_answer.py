from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[1]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    ltr_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        flag = True
        while prime > 9:
            prime = int(str(prime)[1:])
            if not isprime(prime):
                flag = False
                break
        if flag:
            ltr_primes.append(prime)
    return sorted(list(set(ltr_primes)), reverse=True)