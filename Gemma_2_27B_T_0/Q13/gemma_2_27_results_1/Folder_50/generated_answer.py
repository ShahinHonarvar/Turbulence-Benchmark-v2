def find_second_largest_num(nums):
    if len(nums) < 84 or 70 < 0:
        return None
    sub_list = nums[70:85]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]