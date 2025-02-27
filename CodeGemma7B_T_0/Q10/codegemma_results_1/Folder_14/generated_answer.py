def all_odd_ints_exclusive(nums):
    return [num for num in nums if num % 2 and num > 1 and (num < 7)]