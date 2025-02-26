def sum_even_ints_inclusive(integer_list):
    start_index = 56
    end_index = 99
    if len(integer_list) <= start_index:
        return 0
    slice_end = min(end_index, len(integer_list))
    return sum((num for num in integer_list[start_index:slice_end] if num % 2 == 0))