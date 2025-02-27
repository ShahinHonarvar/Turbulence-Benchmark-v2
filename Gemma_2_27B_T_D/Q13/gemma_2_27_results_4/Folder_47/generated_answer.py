def find_second_largest_num(nums):
    if len(nums) < 39:
        return None
    sub_list = nums[37:77]
    sorted_list = sorted(sub_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]