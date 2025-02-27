def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    sublist = sorted(nums[17:79])
    if len(sublist) < 2:
        return None
    return sublist[1]