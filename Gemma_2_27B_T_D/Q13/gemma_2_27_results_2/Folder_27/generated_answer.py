def find_second_largest_num(nums):
    sub_list = nums[66:94]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list))[-2]