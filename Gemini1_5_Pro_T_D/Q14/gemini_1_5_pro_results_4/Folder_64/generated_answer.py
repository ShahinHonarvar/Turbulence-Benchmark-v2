def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 5:
        return None
    else:
        ordered = sorted(nums[:5])
        return ordered[1]