def sum_even_ints_inclusive(integer_list):
    start_index = 30
    end_index = 200
    sum_even = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            sum_even += integer_list[i]
    return sum_even