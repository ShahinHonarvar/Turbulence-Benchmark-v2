def gcf_two_nums(ints):
    a = ints[47]
    b = ints[97]
    while b:
        a, b = (b, a % b)
    return a