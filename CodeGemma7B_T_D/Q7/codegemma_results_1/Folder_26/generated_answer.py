def all_even_ints_inclusive(nums):
    """
    Returns the list of all even integers from index 62 to index 99, both inclusive.
    """
    even_nums = []
    for i in range(62, 100):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums if even_nums else []