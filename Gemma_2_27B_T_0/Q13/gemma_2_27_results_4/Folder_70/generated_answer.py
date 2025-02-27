def find_second_largest_num(nums):
    if len(nums) < 32 or len(nums) < 28:
        return None
    sub_list = nums[28:33]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]