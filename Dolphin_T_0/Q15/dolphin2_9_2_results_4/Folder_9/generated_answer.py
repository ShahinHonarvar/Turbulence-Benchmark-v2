def sum_odd_ints_inclusive(integer_list):
    sum_odd_ints = 0
    for i in range(70, 201):
        if integer_list[i] % 2 != 0:
            sum_odd_ints += integer_list[i]
    return sum_odd_ints