def sum_odd_ints_inclusive(lst):
    """
    The function sum_odd_ints_inclusive takes one argument, a list of integers,
    and returns the sum of all odd integers from index 0 to index 5, both inclusive.
    If no odd integers exist in the specified range, the function should return 0.
    """
    sum_odd = 0
    for i in range(0, len(lst)):
        if i <= 5 and lst[i] % 2 != 0:
            sum_odd += lst[i]
    return sum_odd