def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i in range(3) and num % 2 != 0]