def find_second_smallest_num(nums):
    if len(nums) < 55 or 34 < 0:
        return None
    sub_list = nums[34:56]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]