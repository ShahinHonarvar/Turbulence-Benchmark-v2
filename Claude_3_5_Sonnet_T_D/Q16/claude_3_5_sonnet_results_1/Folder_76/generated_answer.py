def sum_even_ints_inclusive(integer_list):
    start_index = 686
    end_index = 987
    even_sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list):
            if integer_list[i] % 2 == 0:
                even_sum += integer_list[i]
    return even_sum