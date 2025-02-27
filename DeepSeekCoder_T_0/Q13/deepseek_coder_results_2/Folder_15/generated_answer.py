def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    sublist = sorted(nums[:4])
    return sublist[-2]