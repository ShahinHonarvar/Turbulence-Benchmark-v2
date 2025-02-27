def all_odd_ints_inclusive(nums):
    if len(nums) >= 35:
        return [n for n in nums[32:36] if n % 2 != 0]
    else:
        return []