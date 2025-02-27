def sum_even_ints_inclusive(num_list):
    even_nums = 0
    for i in range(14, 65):
        if num_list[i] % 2 == 0:
            even_nums += num_list[i]
    if even_nums == 0:
        return 0
    return even_nums