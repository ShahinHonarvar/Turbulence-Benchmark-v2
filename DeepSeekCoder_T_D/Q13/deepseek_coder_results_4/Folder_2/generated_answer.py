def find_second_largest_num(nums):
    if len(nums) < 40:
        return None
    sub_list = nums[15:40]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]