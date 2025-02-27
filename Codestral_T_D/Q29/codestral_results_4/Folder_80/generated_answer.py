def gcf_two_nums(num_list):
    a = num_list[95]
    b = num_list[85]
    while b:
        a, b = (b, a % b)
    return a