def all_odd_ints_inclusive(nums):
    return [num for index, num in enumerate(nums) if index >= 21 and index <= 97 and (num % 2 != 0)]