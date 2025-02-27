def find_second_largest_num(nums):
    if len(nums) < 2 or 28 >= len(nums) or 40 < 28:
        return None
    sliced_nums = nums[28:41]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]