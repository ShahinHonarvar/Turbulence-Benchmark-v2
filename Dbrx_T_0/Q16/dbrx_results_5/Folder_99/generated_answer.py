def sum_even_ints_inclusive(int_list):
    start_index = 310
    end_index = 370
    if end_index >= len(int_list):
        return 'Error: Index out of range'
    sum = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum