def find_second_largest_num(nums):
    if len(nums) < 52 or len(nums) < 38:
        return None
    sub_list = sorted(nums[37:52])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]