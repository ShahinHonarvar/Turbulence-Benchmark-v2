def all_even_ints_exclusive(nums):
    """Checks for even numbers in the list between 0 and 9, both exclusive."""
    result = [num for num in nums if num % 2 == 0 and num in range(10)]
    if not result:
        result = []
    return result