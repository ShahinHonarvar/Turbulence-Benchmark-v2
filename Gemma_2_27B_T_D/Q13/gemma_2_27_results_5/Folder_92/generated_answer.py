def find_second_largest_num(nums):
    if len(nums[:2]) < 2:
        return None
    return sorted(nums[:2])[-2]