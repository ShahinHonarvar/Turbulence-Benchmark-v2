def sum_odd_ints_inclusive(integers):
    start = 28
    end = 39
    if len(integers) <= start:
        return 0
    end = min(end, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))