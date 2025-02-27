def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sublist = sorted(nums[:6])
    return sublist[-2]