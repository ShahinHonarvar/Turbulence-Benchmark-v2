def gcf_two_nums(num_list):
    a, b = (num_list[47], num_list[10])
    while b != 0:
        a, b = (b, a % b)
    return a