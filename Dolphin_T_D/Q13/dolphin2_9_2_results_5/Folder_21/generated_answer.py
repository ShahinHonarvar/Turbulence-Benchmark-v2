def find_second_largest_num(nums):
    sublist = nums[639:976]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    second_max_num = max(sublist)
    return second_max_num