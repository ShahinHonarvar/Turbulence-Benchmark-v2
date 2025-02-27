def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[67:87]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    second_max_num = max(sublist)
    return second_max_num