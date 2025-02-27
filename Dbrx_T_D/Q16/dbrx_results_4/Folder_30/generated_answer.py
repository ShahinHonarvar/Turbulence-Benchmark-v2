def sum_even_ints_inclusive(int_list):
    start_index = 55
    end_index = 98
    if start_index < 0 or end_index >= len(int_list) or start_index > end_index:
        return 'Invalid index range'
    sum_of_even_ints = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum_of_even_ints += int_list[i]
    return sum_of_even_ints