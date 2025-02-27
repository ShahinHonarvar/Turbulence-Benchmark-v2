def sum_even_ints_inclusive(int_list):
    start_index = 66
    end_index = 93
    sum = 0
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        if i >= 0 and i < len(int_list) and (int_list[i] % 2 == 0):
            sum += int_list[i]
    return sum