def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(3, 10):
        if i in int_list and (i % 6 == 0 or i % 1 == 0):
            sum += i
    return sum