def composite_nums_between_indices(nums):
    return {num for num in nums[70:201] if any((num % i == 0 for i in range(2, num)))}