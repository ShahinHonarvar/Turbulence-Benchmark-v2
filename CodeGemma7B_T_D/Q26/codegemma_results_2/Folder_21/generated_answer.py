def sum_in_range(lst):
    sum_of_values = 0
    for val in lst:
        if val in range(138, 859):
            sum_of_values += val
    return sum_of_values