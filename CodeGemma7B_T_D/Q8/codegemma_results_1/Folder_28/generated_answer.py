def all_even_ints_exclusive(nums):
    """The function takes an argument `nums`, which contains a list of integers.
    The function checks for all the even numbers from index 20 to 51 in `nums`, both exclusive.
    The function returns an empty list if no even numbers are found in the specified range."""
    return [num for num in nums[20:51] if num % 2 == 0]