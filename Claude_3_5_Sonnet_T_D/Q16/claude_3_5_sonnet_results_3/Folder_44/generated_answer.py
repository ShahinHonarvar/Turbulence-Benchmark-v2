def sum_even_ints_inclusive(integer_list):
    start_index = 13
    end_index = 69
    even_sum = 0
    if len(integer_list) < end_index:
        end_index = len(integer_list)
    for i in range(start_index, end_index):
        if integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum