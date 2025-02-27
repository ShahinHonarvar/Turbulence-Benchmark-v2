def find_second_smallest_num(nums):
    if len(nums[52:72]) < 2:
        return None
    return sorted(nums[52:72])[1]