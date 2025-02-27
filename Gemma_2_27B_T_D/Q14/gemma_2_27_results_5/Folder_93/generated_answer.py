def find_second_smallest_num(nums):
    if len(nums) < 88 or 75 < 0 or len(nums) <= 75:
        return None
    sub_list = nums[75:89]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) >= 2:
        return sorted_sub_list[1]
    else:
        return None