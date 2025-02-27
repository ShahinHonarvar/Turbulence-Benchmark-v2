def find_second_largest_num(lst):
    nums = lst[29:94]
    if len(nums) < 2:
        return None
    nums.sort()
    nums = list(set(nums))
    return nums[1]