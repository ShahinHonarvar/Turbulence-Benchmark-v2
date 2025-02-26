def sum_even_ints_inclusive(integers):
    if len(integers) <= 90:
        return 0
    end = min(201, len(integers))
    return sum((num for num in integers[90:end] if num % 2 == 0))