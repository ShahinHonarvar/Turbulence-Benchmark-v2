def sum_even_ints_inclusive(integer_list):
    start_index = 5
    end_index = 7
    sum_of_even_ints = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            sum_of_even_ints += integer_list[i]
    return sum_of_even_ints