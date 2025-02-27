def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i in range(6, 9) and num % 2 == 1]