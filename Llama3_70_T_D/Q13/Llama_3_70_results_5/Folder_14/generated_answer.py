def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    nums = lst[5:8]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]