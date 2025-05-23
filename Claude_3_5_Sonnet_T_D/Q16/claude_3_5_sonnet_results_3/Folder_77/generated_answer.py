def sum_even_ints_inclusive(integers):
    start = 527
    end = 539
    if len(integers) <= start:
        return 0
    slice_end = min(end, len(integers))
    return sum((num for num in integers[start:slice_end] if num % 2 == 0))