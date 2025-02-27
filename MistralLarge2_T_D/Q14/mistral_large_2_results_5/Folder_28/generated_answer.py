def find_second_smallest_num(nums):
    if len(nums) < 51:
        return None
    sublist = sorted(nums[22:51])
    if len(sublist) < 2:
        return None
    return sublist[1]