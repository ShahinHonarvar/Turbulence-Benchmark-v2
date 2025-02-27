def all_even_ints_exclusive(nums):
    """
            Write a function called 'all_even_ints_exclusive' that takes one argument, a list of integers, and returns the list of all even integers from index 23 to index 45, both exclusive. If no even integers exist in the specified range, the function should return an empty list.
            """
    even_nums = []
    for num in nums[23:45]:
        if num % 2 == 0:
            even_nums.append(num)
    if not even_nums:
        return []
    return even_nums