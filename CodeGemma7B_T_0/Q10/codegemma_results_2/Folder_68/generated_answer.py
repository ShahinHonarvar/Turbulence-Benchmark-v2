def all_odd_ints_exclusive(nums):
    return [num for num in nums if num % 2 and num in range(0, 9)]