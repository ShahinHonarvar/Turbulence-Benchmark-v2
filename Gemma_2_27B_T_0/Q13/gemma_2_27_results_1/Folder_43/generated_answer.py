def find_second_largest_num(nums):
    if len(nums) < 86 or len(nums) < 68:
        return None
    sub_list = nums[68:87]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]