def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    sublist = sorted(nums[:10])
    return sublist[-2] if len(sublist) > 1 else None