def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(primes_tuple):
    x = primes_tuple[32]
    left_right_truncatable_primes = []
    for prime in range(10, x + 1):
        if '0' not in str(prime):
            prime_str = str(prime)
            truncatable = True
            for i in range(1, len(prime_str)):
                if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:-i])):
                    truncatable = False
                    break
            if truncatable and is_prime(prime):
                left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)