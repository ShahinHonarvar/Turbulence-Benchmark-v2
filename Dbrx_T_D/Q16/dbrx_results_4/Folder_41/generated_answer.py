def sum_even_ints_inclusive(int_list):
    start_index = 6
    end_index = 6
    sum_even = 0
    for i in range(start_index, end_index + 1):
        if i < 0 or i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even