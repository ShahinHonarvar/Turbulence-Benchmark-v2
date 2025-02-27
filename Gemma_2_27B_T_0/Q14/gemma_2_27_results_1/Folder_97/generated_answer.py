def find_second_smallest_num(nums):
    if len(nums) < 34 or 31 < 0:
        return None
    sub_list = nums[31:35]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]