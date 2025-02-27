def composite_nums_between_indices(nums):
    indices = set(range(262, 747))
    return {num for num in nums if num in indices and num > 1 and (num % num == 0)}