def composite_nums_between_indices(nums):
    composites = {num for num in nums[686:988] if num not in [2, 3, 5, 7] and any((num % i == 0 for i in range(2, num)))}
    return composites if composites else set()