def all_right_truncatable_prime(tup):
    x = tup[32]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            truncated_prime = int(str_prime[:-i])
            if truncated_prime in primes:
                right_truncatable_primes.append(prime)
                break
    return sorted(right_truncatable_primes)