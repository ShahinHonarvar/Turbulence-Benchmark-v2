from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[992]
    rtp_primes = []
    for num in range(1, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            rtp_primes.append(num)
    return sorted(rtp_primes)