from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[39]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    result = []
    for prime in primes:
        if '0' in str(prime):
            continue
        is_lr_truncatable = True
        for i in range(len(str(prime)) - 1):
            if not isprime(int(str(prime)[i:])):
                is_lr_truncatable = False
                break
        if is_lr_truncatable:
            result.append(prime)
    return sorted(result, reverse=True)