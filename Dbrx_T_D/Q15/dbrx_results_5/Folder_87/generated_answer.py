def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in int_list[35:47]:
        if i % 2 != 0:
            sum += i
    return sum