def find_second_largest_num(nums):
    sublist = sorted(nums[10:67], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]