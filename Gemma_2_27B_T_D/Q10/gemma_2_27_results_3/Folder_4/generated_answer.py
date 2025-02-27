def all_odd_ints_exclusive(nums):
    return [num for index, num in enumerate(nums) if index >= 10 and index < 76 and (num % 2 != 0)]