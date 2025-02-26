def sum_odd_ints_inclusive(integers):
    start = 50
    end = 201
    if len(integers) <= start:
        return 0
    slice_end = min(end, len(integers))
    return sum((num for num in integers[start:slice_end] if num % 2 != 0))