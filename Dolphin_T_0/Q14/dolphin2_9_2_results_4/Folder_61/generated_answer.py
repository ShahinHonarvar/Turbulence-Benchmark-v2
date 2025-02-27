def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    min1 = min(nums[:8])
    nums.remove(min1)
    if len(nums) == 0:
        return None
    min2 = min(nums[:7])
    return min2