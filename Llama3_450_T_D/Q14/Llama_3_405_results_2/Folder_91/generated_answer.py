def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums[:6]) < 2:
        return None
    return sorted(nums[:6])[1]