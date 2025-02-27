def all_left_right_truncatable_prime(nums):
    primes = [2] * (nums[0] + 1)
    for i in range(3, int(nums[0] ** 0.5) + 1):
        if primes[i]:
            for j in range(i + i, len(primes), i):
                primes[j] = True
    return sorted([p for p in primes if p.is_prime() and p.digits() > 2])