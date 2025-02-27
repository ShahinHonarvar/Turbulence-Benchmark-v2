def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if 40 <= i <= 200 and (not isprime(n))}