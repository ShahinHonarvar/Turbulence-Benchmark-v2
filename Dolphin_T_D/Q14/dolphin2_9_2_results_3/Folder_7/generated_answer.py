def find_second_smallest_num(nums):
    sublist = nums[686:988]
    if len(sublist) >= 2:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]
    else:
        return None