def sum_in_range(list1):
    """
    The sum of all integers from the given list that is between 3 and 9, both inclusive.
    """
    sum = 0
    for i in list1:
        if i >= 3 and i <= 9:
            sum += i
    return sum