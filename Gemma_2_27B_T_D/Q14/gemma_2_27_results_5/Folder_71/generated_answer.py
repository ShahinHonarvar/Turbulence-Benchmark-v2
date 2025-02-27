def find_second_smallest_num(nums):
    if len(nums) < 23:
        return None
    sub_list = nums[29:52]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]