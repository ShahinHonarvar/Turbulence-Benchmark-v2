def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    nums[29:94] = sorted(nums[29:94], reverse=True)
    return nums[29] if len(nums) >= 30 else None