def sum_even_ints_inclusive(integer_list):
    start_index = 28
    end_index = 39
    even_sum = 0
    for i in range(start_index, end_index):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum