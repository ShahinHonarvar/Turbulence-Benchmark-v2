def all_odd_ints_exclusive(nums):
    return [num for num in nums if num % 2 == 1 and 0 < num < 9] or []