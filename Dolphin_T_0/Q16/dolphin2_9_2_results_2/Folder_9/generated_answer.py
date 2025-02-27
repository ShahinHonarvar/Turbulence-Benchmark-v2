def sum_even_ints_inclusive(int_list):
    sum_ = 0
    for i in range(70, 201):
        if int_list[i] % 2 == 0:
            sum_ += int_list[i]
    return sum_