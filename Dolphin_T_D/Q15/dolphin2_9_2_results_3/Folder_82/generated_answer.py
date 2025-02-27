def sum_odd_ints_inclusive(int_list):
    return sum((int_list[i] for i in range(20, 201) if int_list[i] % 2 != 0))