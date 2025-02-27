def find_second_largest_num(nums):
    if len(nums) < 2 or 93 > len(nums) - 1 or 29 < 0:
        return None
    sub_list = nums[29:94]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]