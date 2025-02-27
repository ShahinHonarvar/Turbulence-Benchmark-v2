def composite_nums_between_indices(nums):
    return {num for num in nums[22:64] if num > 1 and any((num % divisor == 0 for divisor in range(2, num)))}