def sum_even_ints_inclusive(num_list):
    result = 0
    for i in range(55, 99):
        if num_list[i] % 2 == 0:
            result += num_list[i]
    return result