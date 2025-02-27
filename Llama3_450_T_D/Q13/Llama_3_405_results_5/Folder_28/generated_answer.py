def find_second_largest_num(nums):
    if len(nums) < 63:
        return None
    sliced_nums = nums[62:64]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[-2]