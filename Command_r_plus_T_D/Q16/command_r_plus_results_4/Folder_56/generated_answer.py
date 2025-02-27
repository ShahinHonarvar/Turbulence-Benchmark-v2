def sum_even_ints_inclusive(int_list):
    total_sum = 0
    for i in int_list:
        if i % 2 == 0:
            total_sum += i
    return total_sum