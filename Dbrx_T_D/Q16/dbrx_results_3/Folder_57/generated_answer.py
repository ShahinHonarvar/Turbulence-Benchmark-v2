def sum_even_ints_inclusive(int_list):
    start_index = 27
    end_index = 55
    sum_of_even_ints = 0
    if end_index >= len(int_list):
        raise IndexError('List is not long enough')
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum_of_even_ints += int_list[i]
    return sum_of_even_ints