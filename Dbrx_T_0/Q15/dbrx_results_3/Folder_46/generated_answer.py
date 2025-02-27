def sum_odd_ints_inclusive(lst):
    if len(lst) < 88:
        return 'Input list is too short. List must have at least 88 elements.'
    else:
        odd_ints = [i for i in lst[30:88] if i % 2 != 0]
        if odd_ints:
            return sum(odd_ints)
        else:
            return 0