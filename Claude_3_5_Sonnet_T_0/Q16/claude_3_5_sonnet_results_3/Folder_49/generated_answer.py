def sum_even_ints_inclusive(integer_list):
    start_index = 8
    end_index = 81
    even_sum = 0
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum