def find_second_smallest_num(nums):
    if len(nums) < 72 or 52 < 0:
        return None
    sub_list = nums[52:72]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]