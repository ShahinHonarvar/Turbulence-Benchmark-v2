def find_second_largest_num(nums):
    if len(nums) < 62:
        return None
    sub_list = nums[16:62]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]