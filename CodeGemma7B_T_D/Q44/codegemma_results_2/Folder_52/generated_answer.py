def composite_nums_between_indices(nums):
    return {num for num in nums[62:100] if num not in {1, 2, 3, 5, 7} and num % sum(range(2, int(num ** 0.5) + 1)) != 0}