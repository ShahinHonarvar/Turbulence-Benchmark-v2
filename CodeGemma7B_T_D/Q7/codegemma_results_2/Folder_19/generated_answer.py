def all_even_ints_inclusive(nums):
    """Return the list of all even integers from index 3 to index 5, both inclusive.
            """
    return [x for x in nums[3:6] if x % 2 == 0]