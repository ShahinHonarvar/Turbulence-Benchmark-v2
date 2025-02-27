def sum_even_ints_inclusive(integer_list):
    start_index = 13
    end_index = 68
    even_ints_sum = 0
    if len(integer_list) < 68:
        return 0
    for i in range(start_index, end_index + 1):
        if i >= len(integer_list):
            break
        if integer_list[i] % 2 == 0:
            even_ints_sum += integer_list[i]
    return even_ints_sum