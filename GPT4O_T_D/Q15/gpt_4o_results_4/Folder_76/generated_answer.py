def sum_odd_ints_inclusive(lst):
    if isinstance(lst, list) and all((isinstance(i, int) for i in lst)) and (len(lst) > 987):
        return sum((i for i in lst[686:988] if i % 2 != 0))
    return 0