def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    sublist = nums[4:5]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None