def find_second_smallest_num(nums):
    if len(nums[:9]) < 2:
        return None
    return sorted(set(nums[:9]))[1]