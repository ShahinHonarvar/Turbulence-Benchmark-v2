def composite_nums_between_indices(nums):
    return {x for x in nums[29:94] if x > 1 and any((x % i == 0 for i in range(2, int(x ** 0.5) + 1)))}