def all_right_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable = True
        n = prime
        while n > 0:
            if n not in primes:
                is_right_truncatable = False
                break
            n //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)