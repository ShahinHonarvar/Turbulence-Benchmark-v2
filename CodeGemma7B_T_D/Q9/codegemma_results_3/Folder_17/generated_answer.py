def all_odd_ints_inclusive(nums):
    """Return a list of odd numbers from index 62 to 78, inclusive."""
    result = [num for num in nums[62:79] if num % 2 != 0]
    return result if result else []