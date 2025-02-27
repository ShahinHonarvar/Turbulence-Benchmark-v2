from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[70]
    prime_numbers = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatable_primes = []
    for prime in prime_numbers:
        if '0' in str(prime):
            continue
        prime_str = str(prime)
        is_truncatable_prime = True
        for i in range(1, len(prime_str)):
            if not isprime(int(prime_str[i:])) or not isprime(int(prime_str[:-i])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)