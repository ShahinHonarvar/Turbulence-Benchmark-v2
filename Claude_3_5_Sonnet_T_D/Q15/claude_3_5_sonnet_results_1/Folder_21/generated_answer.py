def sum_odd_ints_inclusive(integers):
    start = 639
    end = 976
    if len(integers) <= start:
        return 0
    range_end = min(end, len(integers))
    return sum((num for num in integers[start:range_end] if num % 2 != 0))