def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max1 = max(nums)
    nums.remove(max1)
    if len(nums) < 2:
        return None
    max2 = max(nums)
    return max2