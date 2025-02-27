def gcf_two_nums(int_list):
    value1 = int_list[129]
    value2 = int_list[582]
    if value1 < value2:
        small = value1
    else:
        small = value2
    for i in range(small, 1, -1):
        if value1 % i == 0 and value2 % i == 0:
            return i