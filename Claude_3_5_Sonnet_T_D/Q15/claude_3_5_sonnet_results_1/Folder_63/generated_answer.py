def sum_odd_ints_inclusive(integers):
    start = min(22, len(integers))
    end = min(89, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))