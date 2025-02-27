def composite_nums_between_indices(nums):
    return {num for num in nums[20:201] if not num.is_prime()}