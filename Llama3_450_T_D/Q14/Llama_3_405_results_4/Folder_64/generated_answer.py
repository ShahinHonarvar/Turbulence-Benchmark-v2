def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums[:5]) < 2:
        return None
    return sorted(nums[:5])[1]