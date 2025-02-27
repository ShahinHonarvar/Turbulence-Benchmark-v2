from sympy import isprime

def all_left_right_truncatable_prime(upper_limit_tuple):
    x = upper_limit_tuple[14]
    all_primes = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatable_primes = []
    for prime in all_primes:
        if '0' in str(prime):
            continue
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if not isprime(int(prime_str[i:])) or not isprime(int(prime_str[:-i])):
                break
        else:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)