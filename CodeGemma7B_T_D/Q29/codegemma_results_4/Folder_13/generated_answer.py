def gcf_two_nums(num_list):
    a = num_list[534]
    b = num_list[630]
    while b > 0:
        a, b = (b, a % b)
    return a