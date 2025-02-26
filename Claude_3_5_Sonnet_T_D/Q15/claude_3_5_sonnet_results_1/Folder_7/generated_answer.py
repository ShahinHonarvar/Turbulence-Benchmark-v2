def sum_odd_ints_inclusive(integers):
    start = max(661, 0)
    end = min(925, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))