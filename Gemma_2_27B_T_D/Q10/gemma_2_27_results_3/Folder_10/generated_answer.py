def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i in range(48, 74) and num % 2 != 0]