def find_second_largest_num(nums):
    if len(nums) < 31:
        return None
    sliced_nums = nums[20:31]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort(reverse=True)
    return sliced_nums[1]