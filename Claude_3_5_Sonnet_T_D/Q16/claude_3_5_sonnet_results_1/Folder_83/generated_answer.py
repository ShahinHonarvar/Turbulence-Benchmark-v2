def sum_even_ints_inclusive(integer_list):
    start_index = 90
    end_index = 201
    even_sum = 0
    if len(integer_list) <= start_index:
        return 0
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum