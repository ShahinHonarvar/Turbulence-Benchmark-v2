def find_second_smallest_num(nums):
    if len(nums) < 85 or 75 < 0:
        return None
    sub_list = nums[75:86]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]