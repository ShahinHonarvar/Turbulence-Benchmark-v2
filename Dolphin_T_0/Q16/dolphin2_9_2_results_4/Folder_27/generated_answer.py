def sum_even_ints_inclusive(int_list):
    if not int_list:
        return 0
    sum_ = 0
    for i in range(66, 94):
        if i < len(int_list):
            if int_list[i] % 2 == 0:
                sum_ += int_list[i]
    return sum_