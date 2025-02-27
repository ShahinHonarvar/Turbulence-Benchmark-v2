def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    sublist = sorted(nums[:3])
    return sublist[1]