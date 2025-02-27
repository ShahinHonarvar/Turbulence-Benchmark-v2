def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 85:
        return None
    filtered = [num for num in nums[74:86] if num < max(nums[74:86])]
    if len(filtered) < 2:
        return None
    return sorted(filtered)[-2]