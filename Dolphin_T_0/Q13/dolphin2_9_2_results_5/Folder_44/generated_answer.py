def find_second_largest_num(nums):
    sublist = nums[13:69]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max_num = max(sublist)
    return second_max_num