def find_second_largest_num(nums):
    sublist = sorted(nums[75:86], reverse=True)
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]