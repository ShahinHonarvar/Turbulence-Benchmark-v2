def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    sub_list = nums[74:96]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]