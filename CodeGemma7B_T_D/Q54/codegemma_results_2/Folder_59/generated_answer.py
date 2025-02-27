def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for prime in range(2, x):
        if is_prime(prime):
            for k in range(1, len(str(prime))):
                truncated_prime = int(str(prime)[:-k])
                if not is_prime(truncated_prime):
                    break
            else:
                right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)