def find_second_smallest_num(nums):
    sublist = nums[60:201]
    if len(sublist) < 2:
        return None
    min1 = min(sublist)
    sublist.remove(min1)
    if not sublist:
        return None
    return min(sublist)