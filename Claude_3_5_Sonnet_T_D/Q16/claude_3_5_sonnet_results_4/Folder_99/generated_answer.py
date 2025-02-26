def sum_even_ints_inclusive(integers):
    start_index = 310
    end_index = 371
    if len(integers) <= start_index:
        return 0
    slice_end = min(end_index, len(integers))
    return sum((num for num in integers[start_index:slice_end] if num % 2 == 0))