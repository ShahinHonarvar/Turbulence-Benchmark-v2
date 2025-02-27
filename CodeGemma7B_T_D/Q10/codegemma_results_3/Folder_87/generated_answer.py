def all_odd_ints_exclusive(nums):
    return [num for num in nums if num % 2 != 0 and num >= 32 and (num < 99)]