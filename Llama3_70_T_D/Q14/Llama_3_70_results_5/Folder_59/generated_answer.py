def find_second_smallest_num(nums):
    if len(nums[:10]) < 2:
        return None
    return sorted(nums[:10])[1]