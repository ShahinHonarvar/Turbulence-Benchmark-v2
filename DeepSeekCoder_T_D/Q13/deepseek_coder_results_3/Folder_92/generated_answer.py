def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first, second = sorted(nums[:2])
    return second