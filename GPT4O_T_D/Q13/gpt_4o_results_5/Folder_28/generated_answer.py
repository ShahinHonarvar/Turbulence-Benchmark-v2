def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sub_list = nums[62:64]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]