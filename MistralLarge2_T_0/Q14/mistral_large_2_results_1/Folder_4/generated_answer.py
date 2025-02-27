def find_second_smallest_num(nums):
    if len(nums) < 85:
        return None
    sublist = nums[70:85]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]