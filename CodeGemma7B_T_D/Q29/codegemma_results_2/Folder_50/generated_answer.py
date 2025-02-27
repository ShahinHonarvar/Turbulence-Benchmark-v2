def gcf_two_nums(int_list):
    a = int_list[90]
    b = int_list[54]
    greatest_common_factor = 1
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        greatest_common_factor += 1
    return greatest_common_factor