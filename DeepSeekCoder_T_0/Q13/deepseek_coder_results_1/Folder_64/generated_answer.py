def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sublist = sorted(nums[:5])
    return sublist[-2]