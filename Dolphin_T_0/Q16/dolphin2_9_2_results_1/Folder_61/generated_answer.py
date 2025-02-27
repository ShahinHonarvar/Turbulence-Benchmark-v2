def sum_even_ints_inclusive(lst):
    """
    This function takes a list of integers and returns the sum of all even integers from index 0 to index 7, both inclusive.
    If no even integers exist in the specified range, the function returns 0.
    """
    result = 0
    for i in range(8):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result