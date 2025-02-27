def prime_factors(nums):
    factors = set()
    for p in nums[91]:
        while p % 2 == 0:
            factors.add(2)
            p //= 2
        for i in range(3, int(p ** 0.5) + 1, 2):
            while p % i == 0:
                factors.add(i)
                p //= i
        if p > 1:
            factors.add(p)
    return factors