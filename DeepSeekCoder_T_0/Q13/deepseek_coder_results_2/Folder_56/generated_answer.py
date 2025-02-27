def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    return sorted(nums[:1])[0]