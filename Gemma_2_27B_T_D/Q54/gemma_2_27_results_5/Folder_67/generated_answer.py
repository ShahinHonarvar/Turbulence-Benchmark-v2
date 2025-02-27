def all_right_truncatable_prime(nums):
    x = nums[71]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        is_truncatable = True
        n = p
        while n > 0:
            if n not in primes:
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)