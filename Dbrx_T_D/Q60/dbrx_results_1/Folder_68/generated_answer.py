from sympy import isprime

def all_left_right_truncatable_prime(args):
    start, end = args
    primes = [i for i in range(start, end + 1) if isprime(i)]
    lr_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        prime_str = str(prime)
        while len(prime_str) > 1:
            if not isprime(int(prime_str)) or not isprime(int(prime_str[::-1])):
                break
            prime_str = prime_str[1:]
            prime_str = prime_str[:-1]
        else:
            lr_primes.append(prime)
    return sorted(lr_primes, reverse=True)