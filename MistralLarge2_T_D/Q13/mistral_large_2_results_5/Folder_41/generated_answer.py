def find_second_largest_num(nums):
    if len(nums) <= 6:
        return None
    sublist = nums[6:7]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None