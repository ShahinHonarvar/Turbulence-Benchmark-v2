def find_second_largest_num(nums):
    if len(nums) < 80 or 79 - 29 + 1 < 2:
        return None
    sub_list = sorted(nums[29:80])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]