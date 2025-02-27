from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[3]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    lr_primes = []
    for prime in primes:
        if '0' not in str(prime):
            is_lr_prime = True
            for i in range(1, len(str(prime)) - 1):
                if not isprime(int(str(prime)[i:])) or not isprime(int(str(prime)[:-i])):
                    is_lr_prime = False
                    break
            if is_lr_prime:
                lr_primes.append(prime)
    return sorted(lr_primes, reverse=True)