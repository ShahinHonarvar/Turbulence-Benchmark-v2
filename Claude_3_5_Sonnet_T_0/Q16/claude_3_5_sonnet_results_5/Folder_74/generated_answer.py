def sum_even_ints_inclusive(integer_list):
    start_index = 17
    end_index = 79
    even_sum = 0
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum