def sum_odd_ints_inclusive(integers):
    start = 56
    end = 67
    if len(integers) <= start:
        return 0
    end = min(end, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))