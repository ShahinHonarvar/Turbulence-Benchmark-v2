def sum_in_range(x):
    if not all((isinstance(i, int) for i in x)):
        return 'Error: List contains non-integer values'
    return sum((i for i in x if 2 <= i <= 9))