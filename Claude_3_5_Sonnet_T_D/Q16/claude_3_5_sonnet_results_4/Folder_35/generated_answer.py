def sum_even_ints_inclusive(integer_list):
    start_index = 30
    end_index = 49
    if len(integer_list) <= start_index:
        return 0
    slice_end = min(end_index, len(integer_list))
    relevant_slice = integer_list[start_index:slice_end]
    even_sum = sum((num for num in relevant_slice if num % 2 == 0))
    return even_sum