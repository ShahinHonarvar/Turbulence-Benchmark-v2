def sum_even_ints_inclusive(num_list):
    result = 0
    for i in range(20, 31):
        if i < len(num_list) and num_list[i] % 2 == 0:
            result += num_list[i]
    return result