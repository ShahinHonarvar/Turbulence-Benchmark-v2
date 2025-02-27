from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[39]
    right_truncatable_primes = []
    for i in range(2, x):
        if isprime(i):
            num_str = str(i)
            if all((isprime(int(num_str[:j])) for j in range(1, len(num_str) + 1))):
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)