def composite_nums_between_indices(nums):
    if len(nums) < 49:
        return set()
    composite_nums = {num for num in nums[30:49] if num > 1 and any((num % i == 0 for i in range(2, num)))}
    return composite_nums