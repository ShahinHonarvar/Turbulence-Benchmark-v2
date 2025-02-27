def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    nums = sorted(lst[21:98], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]