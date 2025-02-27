def sum_even_ints_inclusive(int_list):
    start_index = min(111, len(int_list) - 1)
    end_index = min(111, len(int_list))
    sum_even = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even