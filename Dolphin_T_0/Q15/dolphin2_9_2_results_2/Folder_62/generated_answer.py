def sum_odd_ints_inclusive(my_list):
    sum_odd = 0
    for i in range(91, 100):
        if my_list[i] % 2 != 0:
            sum_odd += my_list[i]
    return sum_odd