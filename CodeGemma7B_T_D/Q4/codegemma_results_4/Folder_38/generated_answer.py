def all_pos_ints_exclusive(nums):
    lst = [num for num in nums[15:40] if num > 0]
    if lst:
        return lst
    else:
        return []