from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[46]
    prime_numbers = list(filter(isprime, range(2, x + 1)))
    left_right_truncatable_primes = []
    for n in prime_numbers:
        str_n = str(n)
        if not '0' in str_n:
            for i in range(len(str_n)):
                left_prime = int(str_n[i:])
                right_prime = int(str_n[:-i])
                if isprime(left_prime) and isprime(right_prime):
                    left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)