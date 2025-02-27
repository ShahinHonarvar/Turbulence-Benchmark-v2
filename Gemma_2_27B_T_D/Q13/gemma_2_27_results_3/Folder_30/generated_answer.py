def find_second_largest_num(nums):
    if len(nums) < 44:
        return None
    sub_list = nums[55:99]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]