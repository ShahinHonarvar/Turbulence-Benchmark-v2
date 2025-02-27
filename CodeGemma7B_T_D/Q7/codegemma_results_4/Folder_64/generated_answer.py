def all_even_ints_inclusive(nums):
    """
            This function returns all even integers from index 0 to index 4, inclusive.
            """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    if not even_nums:
        return []
    return even_nums[:5]