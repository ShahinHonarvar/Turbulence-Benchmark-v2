def sum_odd_ints_inclusive(lst):
    if len(lst) < 200:
        return 'Input list must have at least 200 elements.'
    else:
        odd_ints = [i for i in lst[20:201] if i % 2 != 0]
        if odd_ints:
            return sum(odd_ints)
        else:
            return 0