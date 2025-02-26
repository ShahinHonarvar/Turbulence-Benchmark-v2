def sum_odd_ints_inclusive(integers):
    if len(integers) <= 50:
        return 0
    end_index = min(201, len(integers))
    return sum((num for num in integers[50:end_index] if num % 2 != 0))