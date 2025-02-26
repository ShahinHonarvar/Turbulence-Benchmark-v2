def sum_odd_ints_inclusive(integers):
    start = 22
    end = min(89, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))