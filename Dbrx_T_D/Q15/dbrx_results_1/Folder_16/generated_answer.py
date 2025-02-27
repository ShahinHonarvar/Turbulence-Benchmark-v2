def sum_odd_ints_inclusive(lst):
    if len(lst) < 37:
        return 'Input list must have at least 37 elements.'
    elif not all((isinstance(i, int) for i in lst)):
        return 'All elements in the input list must be integers.'
    else:
        odd_ints = [i for i in lst[33:37] if i % 2 != 0]
        return sum(odd_ints) if odd_ints else 0