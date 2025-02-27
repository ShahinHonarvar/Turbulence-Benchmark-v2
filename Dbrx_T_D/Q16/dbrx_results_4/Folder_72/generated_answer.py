def sum_even_ints_inclusive(int_list):
    start_index = 29
    end_index = 51
    sum = 0
    if len(int_list) <= end_index:
        return sum
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum