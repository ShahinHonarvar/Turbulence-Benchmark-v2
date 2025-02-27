def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sublist = sorted(nums[:5])
    if len(sublist) < 2:
        return None
    return sublist[1]