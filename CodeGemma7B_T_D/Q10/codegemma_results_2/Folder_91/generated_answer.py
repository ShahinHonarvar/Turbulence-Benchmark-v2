def all_odd_ints_exclusive(nums):
    result = [num for num in nums if num % 2 != 0 and 0 < nums.index(num) < 5]
    return result or []