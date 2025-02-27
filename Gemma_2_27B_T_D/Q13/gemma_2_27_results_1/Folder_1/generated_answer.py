def find_second_largest_num(nums):
    if len(nums) < 72 or 31 < 0:
        return None
    sub_list = nums[31:73]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]