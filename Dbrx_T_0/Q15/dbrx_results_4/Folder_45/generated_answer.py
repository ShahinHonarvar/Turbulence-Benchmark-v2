def sum_odd_ints_inclusive(lst):
    if len(lst) < 200:
        return 'Input list should have at least 200 elements'
    else:
        odd_ints = [i for i in lst[30:201] if i % 2 != 0]
        return sum(odd_ints) if odd_ints else 0