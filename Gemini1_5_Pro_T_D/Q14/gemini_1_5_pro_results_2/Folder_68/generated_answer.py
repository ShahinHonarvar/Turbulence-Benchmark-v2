def find_second_smallest_num(nums):
    if len(nums[:9]) < 2:
        return None
    else:
        return sorted(nums[:9])[1]