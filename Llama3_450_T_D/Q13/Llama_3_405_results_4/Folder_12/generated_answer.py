def find_second_largest_num(lst):
    if len(lst) < 65:
        return None
    nums = sorted(lst[14:65], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]