def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    sub_list = sorted(nums[30:88])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]