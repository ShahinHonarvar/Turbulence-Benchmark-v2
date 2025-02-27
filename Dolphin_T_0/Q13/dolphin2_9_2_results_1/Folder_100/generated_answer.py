def find_second_largest_num(nums):
    sublist = nums[42:69]
    if len(sublist) < 2:
        return None
    first = max(sublist)
    sublist.remove(first)
    second = max(sublist)
    return second