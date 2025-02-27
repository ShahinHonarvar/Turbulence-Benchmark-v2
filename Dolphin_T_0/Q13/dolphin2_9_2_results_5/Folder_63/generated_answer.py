def find_second_largest_num(nums):
    if not 22 <= 88 < len(nums):
        return None
    nums = nums[22:89]
    if len(set(nums)) < 2:
        return None
    nums.sort()
    return nums[-2]