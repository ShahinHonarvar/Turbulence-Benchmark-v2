def find_second_largest_num(nums):
    if len(nums) < 98:
        return None
    sub_list = nums[55:99]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]