def all_odd_ints_inclusive(integers):
    start = min(30, len(integers))
    end = min(201, len(integers))
    return [num for num in integers[start:end] if num % 2 != 0]