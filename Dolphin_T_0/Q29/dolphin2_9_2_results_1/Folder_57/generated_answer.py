def gcf_two_nums(int_list):
    a = int_list[28]
    b = int_list[49]
    if a == 0:
        return b
    elif b == 0:
        return a
    while b:
        a, b = (b, a % b)
    return a