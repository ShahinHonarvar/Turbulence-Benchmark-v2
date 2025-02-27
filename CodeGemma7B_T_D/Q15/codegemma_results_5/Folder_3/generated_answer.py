def sum_odd_ints_inclusive(lst):
    """
            This function takes one argument, a list of integers, and returns the sum of all odd integers from index 62 to index 92, both inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    output = 0
    for i in range(62, 93):
        if lst[i] % 2 != 0:
            output += lst[i]
    return output