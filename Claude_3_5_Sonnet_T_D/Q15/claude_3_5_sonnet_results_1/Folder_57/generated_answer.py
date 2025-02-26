def sum_odd_ints_inclusive(integers):
    start = 27
    end = min(56, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))