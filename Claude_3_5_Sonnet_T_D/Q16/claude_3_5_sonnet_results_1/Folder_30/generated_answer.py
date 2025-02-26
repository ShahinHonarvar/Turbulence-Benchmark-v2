def sum_even_ints_inclusive(integers):
    if len(integers) <= 55:
        return 0
    end = min(99, len(integers))
    return sum((num for num in integers[55:end] if num % 2 == 0))