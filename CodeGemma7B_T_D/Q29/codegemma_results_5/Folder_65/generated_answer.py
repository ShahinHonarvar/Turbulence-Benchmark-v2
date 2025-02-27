def gcf_two_nums(list):
    if len(list) != 97:
        raise ValueError('List should have exactly 97 elements')
    a = list[29]
    b = list[53]
    while b:
        a, b = (b, a % b)
    return a