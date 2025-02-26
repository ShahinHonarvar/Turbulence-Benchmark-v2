def sum_even_ints_inclusive(integers):
    if len(integers) <= 22:
        return 0
    end = min(89, len(integers))
    return sum((num for num in integers[22:end] if num % 2 == 0))