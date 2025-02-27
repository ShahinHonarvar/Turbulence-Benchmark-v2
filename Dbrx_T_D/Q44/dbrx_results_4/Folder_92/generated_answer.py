def composite_nums_between_indices(nums):
    if len(nums) < 2:
        return set()
    return {num for num in nums[1:2] if num > 1 and any((num % div == 0 for div in range(2, num)))}