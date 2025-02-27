def sum_odd_ints_inclusive(nums):
    if not any((num % 2 != 0 for num in nums[22:89])):
        return 0
    return sum((num for num in nums[22:89] if num % 2 != 0))