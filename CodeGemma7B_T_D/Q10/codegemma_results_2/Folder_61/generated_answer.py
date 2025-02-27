def all_odd_ints_exclusive(nums):
    result = [num for num in nums if num % 2 != 0 and num < 8]
    return result if result else []