def all_odd_ints_inclusive(nums):
    return [num for num in nums if num in range(50, 201) and num % 2 != 0]