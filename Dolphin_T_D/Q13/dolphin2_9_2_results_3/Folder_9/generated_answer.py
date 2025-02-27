def find_second_largest_num(nums):
    if len(nums) <= 200:
        return None
    sublist = nums[200:201]
    if len(sublist) == 1:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) == 0:
        return None
    second_max_num = max(sublist)
    return second_max_num