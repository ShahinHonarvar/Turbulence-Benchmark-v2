def find_second_largest_num(nums):
    if len(nums) < 2 or 37 > len(nums) - 1 or 76 < 0:
        return None
    sliced_nums = nums[37:77]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]