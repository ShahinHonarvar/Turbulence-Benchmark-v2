def sum_odd_ints_inclusive(nums):
    return sum((num for num in nums[:9] if num % 2 != 0))