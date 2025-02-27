def gcf_two_nums(num_list):
    a = num_list[48]
    b = num_list[74]
    while b != 0:
        a, b = (b, a % b)
    return a