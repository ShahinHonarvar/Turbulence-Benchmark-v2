def sum_odd_ints_inclusive(lst):
    if not isinstance(lst, list) or not all((isinstance(i, int) for i in lst)):
        raise ValueError('Input must be a list of integers')
    if len(lst) < 93:
        raise IndexError('List must have at least 93 elements')
    odd_ints = [i for i in lst[66:94] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0