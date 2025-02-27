def find_second_largest_num(nums):
    sublist = sorted(nums[310:371], reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None