def all_odd_ints_exclusive(nums):
    odds = [item for item in nums if item % 2 == 1 and 0 <= item <= 10]
    return odds or []