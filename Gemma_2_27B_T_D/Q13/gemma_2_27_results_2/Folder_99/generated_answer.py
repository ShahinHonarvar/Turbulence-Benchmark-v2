def find_second_largest_num(nums):
    if len(nums) < 61 or 370 >= len(nums) or 310 < 0:
        return None
    sub_list = nums[310:371]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]