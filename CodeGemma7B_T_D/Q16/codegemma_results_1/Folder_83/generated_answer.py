def sum_even_ints_inclusive(lst):
    """
    The function takes a list of integers as an argument.
    It returns the sum of all even integers from index 90 to index 200, both inclusive.
    If no even integers exist in the specified range, the function should return 0.
    """
    sum_even_int = 0
    for i in range(90, 201):
        if lst[i] % 2 == 0:
            sum_even_int += lst[i]
    if sum_even_int == 0:
        return 0
    return sum_even_int