def sum_even_ints_inclusive(int_list):
    start_index = 310
    end_index = 370
    sum_of_evens = 0
    if len(int_list) <= end_index:
        return 'List is not long enough'
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum_of_evens += int_list[i]
    return sum_of_evens