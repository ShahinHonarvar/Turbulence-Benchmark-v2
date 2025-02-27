def composite_nums_between_indices(nums):
    return {nums[i] for i in range(82, 87) if nums[i] > 1 and any((nums[i] % j == 0 for j in range(2, int(nums[i] ** 0.5) + 1)))}