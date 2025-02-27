def find_second_largest_num(nums):
    sublist = nums[20:201]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    return max(sublist)