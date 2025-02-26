def sum_even_ints_inclusive(integers):
    start = max(60, 0)
    end = min(201, len(integers))
    return sum((num for num in integers[start:end] if num % 2 == 0))