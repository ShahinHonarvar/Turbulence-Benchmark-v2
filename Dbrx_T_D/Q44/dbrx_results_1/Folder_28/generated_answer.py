def composite_nums_between_indices(nums):
    if len(nums) < 89:
        return set()
    composite_nums = {num for num in nums[22:89] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_nums