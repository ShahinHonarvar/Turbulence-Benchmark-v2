def sum_even_ints_inclusive(integers):
    start = 28
    end = 39
    if len(integers) <= start:
        return 0
    range_end = min(end, len(integers))
    return sum((num for num in integers[start:range_end] if num % 2 == 0))