def find_second_smallest_num(nums):
    if len(nums) < 86:
        return None
    sublist = nums[75:86]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]