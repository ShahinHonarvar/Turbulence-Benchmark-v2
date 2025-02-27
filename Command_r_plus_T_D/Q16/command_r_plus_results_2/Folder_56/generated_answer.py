def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i in int_list:
        if i % 2 == 0:
            sum_even += i
    return sum_even