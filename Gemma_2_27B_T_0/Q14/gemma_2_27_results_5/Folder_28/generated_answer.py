def find_second_smallest_num(nums):
    if len(nums) < 50 or 22 < 0:
        return None
    sub_list = nums[22:51]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]