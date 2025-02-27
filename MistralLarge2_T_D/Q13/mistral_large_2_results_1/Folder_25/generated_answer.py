def find_second_largest_num(nums):
    if len(nums) > 93:
        sub_list = nums[29:94]
        if len(sub_list) >= 2:
            sorted_list = sorted(sub_list, reverse=True)
            return sorted_list[1]
    return None