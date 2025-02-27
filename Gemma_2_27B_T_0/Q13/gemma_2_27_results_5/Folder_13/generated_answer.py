def find_second_largest_num(nums):
    if len(nums) < 88 or 25 < 0:
        return None
    sub_list = nums[25:88]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]