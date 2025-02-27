def composite_nums_between_indices(nums):
    return {num for num in set(nums[667:775]) if not num < 2 or (any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))) and num != i * i)}