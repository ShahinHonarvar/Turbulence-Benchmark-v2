def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    sliced_nums = nums[30:201]
    sliced_nums.sort(reverse=True)
    return sliced_nums[1] if len(sliced_nums) > 1 else None