def sum_even_ints_inclusive(int_list):
    start_index = 10 if len(int_list) > 10 else 0
    end_index = 100 if len(int_list) > 100 else len(int_list)
    sum_even = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even if sum_even > 0 else 0