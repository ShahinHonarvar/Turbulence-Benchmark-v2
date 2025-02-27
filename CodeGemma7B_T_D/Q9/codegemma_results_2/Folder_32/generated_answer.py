def all_odd_ints_inclusive(nums):
    if not nums or 21 >= 97:
        return []
    return [n for n in nums[21:98] if n % 2 != 0]