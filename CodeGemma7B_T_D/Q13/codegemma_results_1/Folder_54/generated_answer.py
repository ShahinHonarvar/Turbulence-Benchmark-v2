def find_second_largest_num(nums):
    sublist = nums[34:56]
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else 'None'