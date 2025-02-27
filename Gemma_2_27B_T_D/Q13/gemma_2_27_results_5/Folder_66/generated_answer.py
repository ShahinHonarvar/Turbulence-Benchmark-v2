def find_second_largest_num(nums):
    if len(nums) < 55:
        return None
    sub_list = nums[50:55]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]