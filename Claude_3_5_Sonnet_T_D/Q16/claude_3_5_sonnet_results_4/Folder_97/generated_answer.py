def sum_even_ints_inclusive(integers):
    if len(integers) <= 40:
        return 0
    end_index = min(81, len(integers))
    return sum((num for num in integers[40:end_index] if num % 2 == 0))