def find_second_largest_num(lst):
    if len(lst) < 55:
        return None
    nums = sorted(lst[50:55], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]