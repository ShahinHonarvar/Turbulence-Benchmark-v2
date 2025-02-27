def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max1 = max(nums[:4])
    nums.remove(max1)
    max2 = max(nums[:3])
    return max2 if max2 != max1 else None