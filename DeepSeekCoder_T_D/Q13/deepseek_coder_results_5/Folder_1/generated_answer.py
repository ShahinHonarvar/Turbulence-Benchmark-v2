def find_second_largest_num(nums):
    if len(nums) < 73:
        return None
    sub_list = sorted(nums[31:73])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]