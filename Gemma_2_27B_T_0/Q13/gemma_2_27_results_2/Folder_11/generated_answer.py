def find_second_largest_num(nums):
    if len(nums) < 51 or 37 < 0:
        return None
    sub_list = nums[37:52]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]