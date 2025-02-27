def find_second_largest_num(nums):
    if len(nums) < 59 - 25 + 1:
        return None
    sub_list = nums[25:60]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]