def find_second_smallest_num(nums):
    if len(nums) < 32 or 28 < len(nums):
        return None
    sub_list = nums[28:33]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]