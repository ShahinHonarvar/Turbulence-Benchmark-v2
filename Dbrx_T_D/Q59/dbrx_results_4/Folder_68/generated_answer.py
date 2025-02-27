from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[1]
    primes = [i for i in range(1, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            is_left_truncatable_prime = True
            for i in range(1, len(str_prime)):
                if not isprime(int(str_prime[i:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)