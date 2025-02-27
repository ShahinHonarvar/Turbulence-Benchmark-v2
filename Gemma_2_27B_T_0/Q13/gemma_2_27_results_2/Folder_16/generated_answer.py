def find_second_largest_num(nums):
    if len(nums) < 36 or len(nums) < 33:
        return None
    sub_list = nums[33:37]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]