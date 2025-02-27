def find_second_largest_num(lst):
    if len(lst) < 51:
        return None
    nums = lst[15:52]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]