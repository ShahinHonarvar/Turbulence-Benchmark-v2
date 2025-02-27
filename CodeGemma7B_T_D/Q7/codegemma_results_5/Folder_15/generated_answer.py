def all_even_ints_inclusive(nums):
    """
    Searches for all even integers from index 0 to index 3 (inclusive) in a list of integers and returns them in a new list if found. Returns an empty list otherwise.
    """
    return [num for num in nums if num % 2 == 0 and nums.index(num) <= 3]