def sum_odd_ints_inclusive(nums):
    odds = [n for n in nums[70:201] if n % 2 != 0]
    if not odds:
        return 0
    return sum(odds)