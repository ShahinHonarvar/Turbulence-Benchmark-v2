def find_second_largest_num(nums):
    if len(nums) < 2 or 98 >= len(nums) or 56 < 0:
        return None
    sub_list = nums[56:99]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]