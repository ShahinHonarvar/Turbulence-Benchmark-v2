def sum_even_ints_inclusive(int_list):
    start_index = 55
    end_index = 98
    even_sum = 0
    if end_index < len(int_list):
        for i in range(start_index, end_index + 1):
            if int_list[i] % 2 == 0:
                even_sum += int_list[i]
        return even_sum
    else:
        return 0