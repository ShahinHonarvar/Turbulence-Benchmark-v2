def find_second_largest_num(nums):
    sublist = sorted(nums[59:98], reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    return None