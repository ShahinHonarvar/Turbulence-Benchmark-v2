def find_second_largest_num(nums):
    if len(nums) < 27:
        return None
    sub_list = nums[26:53]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]