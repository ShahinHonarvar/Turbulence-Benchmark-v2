from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[433]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    ltr_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        flag = True
        while prime > 9:
            if not isprime(prime):
                flag = False
                break
            prime = int(str(prime)[1:]) if len(str(prime)) > 2 else int(str(prime)[1:])
        if flag:
            ltr_primes.append(int(str(prime) + str(t[433])))
    return sorted(list(set(ltr_primes)), reverse=True)