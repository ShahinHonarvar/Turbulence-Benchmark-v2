def sum_even_ints_inclusive(int_list):
    """Returns the sum of all even integers from index 10 to index 66, inclusive. If no even integers exist in the specified range, the function should return 0."""
    even_ints = []
    for i in range(10, 67):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    if even_ints:
        return sum(even_ints)
    else:
        return 0