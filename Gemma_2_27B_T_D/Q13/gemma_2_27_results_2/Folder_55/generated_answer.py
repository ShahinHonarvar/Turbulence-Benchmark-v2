def find_second_largest_num(nums):
    if len(nums[:11]) < 2:
        return None
    return sorted(nums[:11])[-2]