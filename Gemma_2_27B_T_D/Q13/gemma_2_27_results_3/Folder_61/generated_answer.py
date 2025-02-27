def find_second_largest_num(nums):
    if len(nums[:8]) < 2:
        return None
    nums[:8].sort()
    return nums[:8][-2]