def gcf_two_nums(int_list):
    a = int_list[7]
    b = int_list[9]
    while b:
        a, b = (b, a % b)
    return a