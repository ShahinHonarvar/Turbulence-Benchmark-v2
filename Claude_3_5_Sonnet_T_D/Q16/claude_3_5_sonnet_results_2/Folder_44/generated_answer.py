def sum_even_ints_inclusive(integers):
    start = min(13, len(integers))
    end = min(69, len(integers))
    return sum((num for num in integers[start:end] if num % 2 == 0))