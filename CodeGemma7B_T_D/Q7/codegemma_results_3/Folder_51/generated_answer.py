def all_even_ints_inclusive(nums):
    """
                Returns the list of all even integers from index 1 to index 8, both inclusive. An empty list is returned if no even integers exist in the specified range.
                """
    result = []
    for num in nums:
        if num % 2 == 0 and 1 <= num <= 8:
            result.append(num)
    return result