def find_second_largest_num(nums):
    if 200 < len(nums) < 40:
        return None
    sublist = nums[40:201]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    second_max_num = max(sublist)
    return second_max_num