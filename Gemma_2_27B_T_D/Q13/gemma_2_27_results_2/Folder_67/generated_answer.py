def find_second_largest_num(nums):
    if len(nums) < 50 or 22 < 0:
        return None
    sub_list = nums[22:51]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]