def find_second_largest_num(nums):
    if len(nums) < 2 or 32 >= len(nums) or 28 < 0:
        return None
    sliced_nums = nums[28:33]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    else:
        return sliced_nums[-2]