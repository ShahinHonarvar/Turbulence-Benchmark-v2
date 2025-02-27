def gcf_two_nums(my_list):
    a = my_list[90]
    b = my_list[41]
    while b:
        a, b = (b, a % b)
    return a