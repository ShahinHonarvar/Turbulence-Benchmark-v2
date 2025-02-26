def sum_even_ints_inclusive(integer_list):
    start_index = 28
    end_index = 41
    if len(integer_list) <= start_index:
        return 0
    actual_end = min(end_index, len(integer_list))
    return sum((num for num in integer_list[start_index:actual_end] if num % 2 == 0))