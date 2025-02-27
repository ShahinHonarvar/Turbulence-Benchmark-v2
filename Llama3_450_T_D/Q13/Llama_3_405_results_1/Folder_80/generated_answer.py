def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sliced_nums = nums[64:67]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[-2]