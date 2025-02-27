def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 6:
        return None
    else:
        return sorted(nums[:6])[1]