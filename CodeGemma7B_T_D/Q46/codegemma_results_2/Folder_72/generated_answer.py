def gcf_three_nums(list):
    a, b, c = (list[44], list[91], list[42])
    while b != 0:
        c, b = (b, c % b)
    return a