def find_second_smallest_num(nums):
    if len(nums) < 93 - 29 + 1:
        return None
    sub_list = nums[29:94]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]