def all_right_truncatable_prime(nums):
    limit = nums[50]
    primes = [i for i in range(2, limit) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = []
    for prime in primes:
        truncated_prime = prime
        while truncated_prime > 1:
            if truncated_prime in primes:
                right_truncatable_primes.append(truncated_prime)
            truncated_prime //= 10
    return sorted(right_truncatable_primes, reverse=True) or []