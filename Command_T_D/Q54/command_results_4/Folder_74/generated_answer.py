def all_right_truncatable_prime(nums):
    primes = sorted((set(nums) for n in nums if all((n % d for d in range(3, int(n ** 0.5) + 1, 2)))))
    if not primes:
        return []
    return sorted(set((p for p in primes if p < nums[36] and all((p % d == 0 for d in range(3, int(p ** 0.5) + 1, 2))))))