def sum_even_ints_inclusive(int_list):
    start_index = 56
    end_index = 98
    sum_of_evens = 0
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum_of_evens += int_list[i]
    return sum_of_evens