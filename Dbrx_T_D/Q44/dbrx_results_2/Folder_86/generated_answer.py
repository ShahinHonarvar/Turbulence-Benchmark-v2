def composite_nums_between_indices(nums):
    return {n for n in nums[43:87] if n > 1 and (not all((n % i for i in range(2, int(n ** 0.5) + 1))))}