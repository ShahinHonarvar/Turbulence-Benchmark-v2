def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums[30:88]) if num > 1 and any((num % j == 0 for j in range(2, int(num ** 0.5) + 1)))}