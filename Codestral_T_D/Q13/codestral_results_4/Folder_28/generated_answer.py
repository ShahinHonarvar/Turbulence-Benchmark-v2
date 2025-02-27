def find_second_largest_num(nums):
    if 62 < len(nums) - 1 and 63 < len(nums) - 1:
        sliced_nums = nums[62:64]
        sliced_nums.sort(reverse=True)
        if len(sliced_nums) > 1:
            return sliced_nums[1]
    return None