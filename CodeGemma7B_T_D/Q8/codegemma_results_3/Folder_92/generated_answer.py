def all_even_ints_exclusive(num_list):
    """
    This function takes one argument, a list of integers, and returns the list of all even integers from
    index 0 to index 1, both exclusive. If no even integers exist in the specified range, the function
    should return an empty list.
    """
    even_nums = []
    for num in num_list:
        if num % 2 == 0 and num != 0:
            even_nums.append(num)
    return even_nums