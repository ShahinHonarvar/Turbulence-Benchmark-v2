def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    sub_list = nums[13:69]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]