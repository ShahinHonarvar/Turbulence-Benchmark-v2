def gcf_two_nums(my_list):
    a = my_list[23]
    b = my_list[45]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a