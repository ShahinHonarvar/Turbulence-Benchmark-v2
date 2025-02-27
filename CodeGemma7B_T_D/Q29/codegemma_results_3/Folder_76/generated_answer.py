def gcf_two_nums(num_list):
    a = num_list[184]
    b = num_list[307]
    while b:
        a, b = (b, a % b)
    return a