def sum_even_ints_inclusive(integer_list):
    start_index = 246
    end_index = 751
    if len(integer_list) <= start_index:
        return 0
    end_index = min(end_index, len(integer_list))
    return sum((num for num in integer_list[start_index:end_index] if num % 2 == 0))