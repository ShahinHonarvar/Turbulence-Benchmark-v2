def gcf_two_nums(my_list):
    a = my_list[90]
    b = my_list[54]
    while b != 0:
        a, b = (b, a % b)
    return a