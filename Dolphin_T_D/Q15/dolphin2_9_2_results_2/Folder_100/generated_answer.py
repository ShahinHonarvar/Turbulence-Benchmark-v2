def sum_odd_ints_inclusive(my_list):
    sum_odd_ints = 0
    for i in range(42, 69):
        if my_list[i] % 2 != 0:
            sum_odd_ints += my_list[i]
    return sum_odd_ints