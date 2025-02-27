def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if num % 2 != 0 and 25 < i < 80]