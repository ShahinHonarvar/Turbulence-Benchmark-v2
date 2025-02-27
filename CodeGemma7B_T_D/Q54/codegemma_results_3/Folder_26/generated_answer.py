def all_right_truncatable_prime(nums):
    x = nums[81]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            truncation = int(str_prime[:-i])
            if truncation in primes:
                truncatable_primes.append(prime)
                break
    return sorted(truncatable_primes, reverse=True)