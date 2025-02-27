def find_second_largest_num(lst):
    if not lst or len(lst) < 85:
        return None
    nums = lst[70:85]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]