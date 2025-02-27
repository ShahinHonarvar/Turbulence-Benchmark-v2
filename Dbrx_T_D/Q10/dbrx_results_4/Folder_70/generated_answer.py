def all_odd_ints_exclusive(nums):
    if len(nums) < 82:
        return []
    else:
        return [n for n in nums[38:81] if n % 2 != 0]