def sum_even_ints_inclusive(lst):
    if len(lst) < 93:
        return 'Input list is too short'
    else:
        even_ints = [i for i in lst[29:94] if i % 2 == 0]
        if even_ints:
            return sum(even_ints)
        else:
            return 0