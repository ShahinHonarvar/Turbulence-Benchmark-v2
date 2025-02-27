def find_second_smallest_num(nums):
    sublist = nums[209:557]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]