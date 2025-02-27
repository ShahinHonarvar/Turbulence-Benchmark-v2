def find_second_smallest_num(nums):
    if len(nums) < 34:
        return None
    sublist = nums[31:35]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]