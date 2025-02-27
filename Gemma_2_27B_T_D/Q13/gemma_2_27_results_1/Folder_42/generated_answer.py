def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    sub_list = nums[29:80]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]