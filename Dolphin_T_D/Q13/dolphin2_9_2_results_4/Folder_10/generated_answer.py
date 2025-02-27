def find_second_largest_num(nums):
    if 59 < len(nums) < 25:
        return None
    else:
        sublist = nums[25:60]
        sublist.sort(reverse=True)
        return sublist[1] if len(sublist) > 1 else None