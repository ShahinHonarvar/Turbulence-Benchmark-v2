def composite_nums_between_indices(nums):
    composite_set = {num for i, num in enumerate(nums[14:65]) if i == 14 or (num > 1 and all((num % j != 0 for j in range(2, num))))} if len(nums) > 64 else set()
    return composite_set