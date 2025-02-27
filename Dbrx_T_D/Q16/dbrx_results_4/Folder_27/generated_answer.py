def sum_even_ints_inclusive(int_list):
    start_index = 66
    end_index = 93
    sum_of_evens = 0
    for i in range(start_index, end_index + 1):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_of_evens += int_list[i]
    return sum_of_evens if sum_of_evens > 0 else 0