def composite_nums_between_indices(nums):
    return {num for num in nums[36:47] if num > 1 and (not any((num % divisor == 0 for divisor in range(2, int(num ** 0.5) + 1)))) if num > 1}