def sum_odd_ints_inclusive(int_list):
    return sum((int_list[i] for i in range(15, 40) if int_list[i] % 2 == 1))