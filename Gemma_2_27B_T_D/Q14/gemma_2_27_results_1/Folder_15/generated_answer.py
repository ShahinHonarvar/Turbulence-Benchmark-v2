def find_second_smallest_num(nums):
    if len(nums[:4]) < 2:
        return None
    else:
        return sorted(nums[:4])[1]