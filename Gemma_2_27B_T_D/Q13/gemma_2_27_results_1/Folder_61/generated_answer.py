def find_second_largest_num(nums):
    if len(nums[:8]) < 2:
        return None
    return sorted(nums[:8])[-2]