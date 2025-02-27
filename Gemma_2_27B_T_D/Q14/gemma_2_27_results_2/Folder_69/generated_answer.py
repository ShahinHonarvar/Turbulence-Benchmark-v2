def find_second_smallest_num(nums):
    if len(nums) < 87 or 25 < len(nums):
        return None
    sub_list = sorted(nums[25:87 + 1])
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None