def sum_even_ints_inclusive(nums):
    """
            Sum all even integers from index 64 to index 66 inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all even integers from index 64 to index 66 inclusive.
            """
    even_nums = [num for num in nums[64:67] if num % 2 == 0]
    if not even_nums:
        return 0
    return sum(even_nums)