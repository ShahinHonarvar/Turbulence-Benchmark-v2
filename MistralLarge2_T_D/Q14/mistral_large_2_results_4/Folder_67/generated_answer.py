def find_second_smallest_num(nums):
    sublist = nums[50:55]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]