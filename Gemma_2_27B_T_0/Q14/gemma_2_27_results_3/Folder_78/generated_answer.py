def find_second_smallest_num(nums):
    if len(nums) < 78 or 17 < 0:
        return None
    sub_list = nums[17:79]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]