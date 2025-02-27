def sum_even_ints_inclusive(integer_list):
    start_index = 661
    end_index = 924
    sum_of_evens = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            sum_of_evens += integer_list[i]
    return sum_of_evens if sum_of_evens > 0 else 0