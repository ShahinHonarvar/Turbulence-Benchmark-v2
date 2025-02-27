def find_second_smallest_num(nums):
    sublist = sorted(nums[686:988])
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None