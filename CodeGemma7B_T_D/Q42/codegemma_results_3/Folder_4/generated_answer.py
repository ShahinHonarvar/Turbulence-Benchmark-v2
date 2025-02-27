def prime_factors(nums):
    s = set()
    for i in range(2, nums[15] + 1):
        while nums[15] % i == 0:
            s.add(i)
            nums[15] //= i
    return s