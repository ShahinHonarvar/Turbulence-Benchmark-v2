def sum_even_ints_inclusive(my_list):
    my_list = my_list[35:50]
    even_sum = sum([i for i in my_list if i % 2 == 0])
    return even_sum or 0