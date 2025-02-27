def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sub_list = nums[75:95]
    if len(sub_list) < 2:
        return None
    return sorted(set(sub_list))[-2]