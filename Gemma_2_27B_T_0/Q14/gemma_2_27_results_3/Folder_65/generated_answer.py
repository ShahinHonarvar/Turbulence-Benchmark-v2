def find_second_smallest_num(nums):
    if len(nums) < 57 or 56 < 0:
        return None
    sub_list = nums[56:58]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]