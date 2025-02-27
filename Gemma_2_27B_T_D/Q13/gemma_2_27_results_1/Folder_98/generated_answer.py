def find_second_largest_num(nums):
    if len(nums[:7]) < 2:
        return None
    return sorted(nums[:7])[-2]