def gcf_two_nums(lst):
    if len(lst) != 2:
        raise ValueError('Input list must have exactly 2 elements')
    if not all((isinstance(i, int) and i > 0 for i in lst)):
        raise ValueError('List must contain exactly 2 positive integers')
    a, b = lst
    while b != 0:
        a, b = (b, a % b)
    return a