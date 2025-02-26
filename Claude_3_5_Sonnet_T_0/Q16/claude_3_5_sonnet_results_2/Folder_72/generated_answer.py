def sum_even_ints_inclusive(integer_list):
    start_index = 29
    end_index = 52
    even_sum = 0
    if len(integer_list) > start_index:
        for num in integer_list[start_index:end_index]:
            if num % 2 == 0:
                even_sum += num
    return even_sum