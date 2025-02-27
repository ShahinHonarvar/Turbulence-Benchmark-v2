def find_second_largest_num(nums):
    if len(nums[:6]) < 2:
        return None
    return sorted(nums[:6])[-2]