def all_odd_ints_exclusive(nums):
    start, end = (323, 972)
    return [num for num in nums[start:end] if num % 2 != 0]