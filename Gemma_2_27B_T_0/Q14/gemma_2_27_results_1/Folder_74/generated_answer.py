def find_second_smallest_num(nums):
    if len(nums) < 46 or 36 < 0:
        return None
    sub_list = nums[36:47]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]