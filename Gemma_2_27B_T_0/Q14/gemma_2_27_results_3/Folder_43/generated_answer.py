def find_second_smallest_num(nums):
    if len(nums) < 95 or 74 < 0:
        return None
    sub_list = nums[74:96]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]