def find_second_largest_num(nums):
    if len(nums) < 93:
        return None
    sliced_nums = nums[12:93]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) > 1:
        return sliced_nums[1]
    return None