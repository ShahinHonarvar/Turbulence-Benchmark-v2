def sum_even_ints_inclusive(int_list):
    start_index = 43
    end_index = 51
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum