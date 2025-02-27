def find_second_smallest_num(nums):
    sublist = nums[36:47]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]