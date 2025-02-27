def sum_even_ints_inclusive(num_list):
    sum_even_nums = sum([x for i, x in enumerate(num_list) if i in range(4) and x % 2 == 0])
    return sum_even_nums