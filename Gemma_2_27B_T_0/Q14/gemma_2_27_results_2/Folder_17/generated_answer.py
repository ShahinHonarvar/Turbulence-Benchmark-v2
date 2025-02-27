def find_second_smallest_num(nums):
    if len(nums) < 38 or len(nums) < 28:
        return None
    sub_list = nums[28:39]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]