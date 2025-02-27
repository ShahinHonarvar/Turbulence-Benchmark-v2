def find_second_smallest_num(nums):
    sublist = sorted(nums[66:94])
    if len(sublist) < 2:
        return None
    return sublist[1]