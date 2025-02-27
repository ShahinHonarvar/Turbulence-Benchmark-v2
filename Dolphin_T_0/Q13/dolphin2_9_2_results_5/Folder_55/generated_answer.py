def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max1 = max(nums[:11])
    nums.remove(max1)
    if len(nums) < 2:
        return None
    max2 = max(nums[:11])
    return max2