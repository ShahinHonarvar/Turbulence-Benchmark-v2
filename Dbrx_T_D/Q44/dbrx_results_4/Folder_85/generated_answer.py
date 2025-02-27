def composite_nums_between_indices(nums):
    if len(nums) < 6:
        return set()
    composite_nums = {num for num in nums[3:6] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums