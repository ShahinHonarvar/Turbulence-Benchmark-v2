def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sliced_nums = nums[55:99]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[-2]