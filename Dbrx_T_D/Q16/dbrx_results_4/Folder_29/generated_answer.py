def sum_even_ints_inclusive(int_list):
    start_index = 59
    end_index = 97
    if end_index >= len(int_list):
        return 0
    sum_of_evens = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum_of_evens += int_list[i]
    return sum_of_evens