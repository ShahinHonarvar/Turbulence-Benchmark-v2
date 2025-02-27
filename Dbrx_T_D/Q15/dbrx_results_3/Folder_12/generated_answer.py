def sum_odd_ints_inclusive(nums):
    odds = [n for n in nums[14:65] if n % 2 != 0]
    return sum(odds) if odds else 0