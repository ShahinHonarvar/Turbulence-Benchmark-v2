def sum_odd_ints_inclusive(integer_list):
    sum_of_odd_ints = 0
    for i in range(62, 64):
        if i >= len(integer_list):
            return 0
        if integer_list[i] % 2 != 0:
            sum_of_odd_ints += integer_list[i]
    return sum_of_odd_ints