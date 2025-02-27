def find_second_smallest_num(nums):
    if len(nums) < 40 or 28 < 0:
        return None
    sub_list = nums[28:41]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]