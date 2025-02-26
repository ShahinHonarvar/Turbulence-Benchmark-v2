def sum_even_ints_inclusive(integers):
    start = min(10, len(integers))
    end = min(67, len(integers))
    return sum((num for num in integers[start:end] if num % 2 == 0))