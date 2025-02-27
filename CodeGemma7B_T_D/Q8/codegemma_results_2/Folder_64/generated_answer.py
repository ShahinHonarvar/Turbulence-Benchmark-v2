def all_even_ints_exclusive(nums):
    """
    This function returns a list of all even integers from 0 to 4, exclusive.
    """
    results = []
    for num in nums:
        if num % 2 == 0 and num >= 0 and (num < 5):
            results.append(num)
    return results