from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[57]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    left_right_primes = []
    for prime in primes:
        if '0' not in str(prime):
            prime_str = str(prime)
            left_truncatable = [int(prime_str[i:]) for i in range(len(prime_str))]
            right_truncatable = [int(prime_str[:i]) for i in range(1, len(prime_str) + 1)]
            if all((isprime(num) for num in left_truncatable)) and all((isprime(num) for num in right_truncatable)):
                left_right_primes.append(prime)
    return sorted(left_right_primes, reverse=True)