def all_odd_ints_inclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 10 and idx <= 66 and (num % 2 != 0)]