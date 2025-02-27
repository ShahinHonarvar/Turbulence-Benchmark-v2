def composite_nums_between_indices(nums):
    if len(nums) < 88 or not all((num > 0 for num in nums)):
        return set()
    composite_nums = {num for num in nums[30:88] if num > 1 and (not all((num % div == 0 for div in range(2, num))))}
    return composite_nums if composite_nums else set()