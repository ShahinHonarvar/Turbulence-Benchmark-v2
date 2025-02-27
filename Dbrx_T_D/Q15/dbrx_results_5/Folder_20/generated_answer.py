def sum_odd_ints_inclusive(lst):
    try:
        odd_ints = [i for i in lst[56:67] if i % 2 != 0]
        return sum(odd_ints) if odd_ints else 0
    except IndexError:
        return 'Error: List index out of range'