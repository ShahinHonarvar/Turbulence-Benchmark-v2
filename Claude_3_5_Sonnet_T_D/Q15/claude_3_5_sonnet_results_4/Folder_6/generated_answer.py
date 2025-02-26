def sum_odd_ints_inclusive(integers):
    start = 10
    end = min(67, len(integers))
    return sum((num for num in integers[start:end] if num % 2 != 0))