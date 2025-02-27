def find_second_largest_num(nums):
    if len(nums) < 2 or 74 >= len(nums) or 95 < 0:
        return None
    sliced_nums = nums[74:96]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]