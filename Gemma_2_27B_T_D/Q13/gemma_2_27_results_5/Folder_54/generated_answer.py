def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    sub_nums = nums[34:56]
    sub_nums.sort()
    if len(sub_nums) < 2:
        return None
    return sub_nums[-2]