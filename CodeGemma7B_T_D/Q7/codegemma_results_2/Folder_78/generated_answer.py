def all_even_ints_inclusive(nums):
    """
            Returns the list of all even integers from index 43 to index 51, both inclusive.

            Args:
                nums: A list of integers.

            Returns:
                A list of even integers from index 43 to index 51, both inclusive. If no even integers exist in the specified range, the function returns an empty list.
            """
    even_nums = []
    for i in range(43, 52):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums