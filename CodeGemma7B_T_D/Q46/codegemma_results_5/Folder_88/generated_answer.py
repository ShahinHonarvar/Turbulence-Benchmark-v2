def gcf_three_nums(num_list):
    a = num_list[47]
    b = num_list[10]
    c = num_list[28]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a