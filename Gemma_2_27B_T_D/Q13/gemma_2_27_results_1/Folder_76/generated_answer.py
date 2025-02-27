def find_second_largest_num(nums):
    sub_list = nums[686:988]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]