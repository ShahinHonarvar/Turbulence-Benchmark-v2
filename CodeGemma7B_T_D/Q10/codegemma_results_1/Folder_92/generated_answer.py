def all_odd_ints_exclusive(nums):
    return [n for n in nums if n % 2 and n >= 0 and (n <= 1)]