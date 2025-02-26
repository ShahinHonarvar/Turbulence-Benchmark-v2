def all_neg_ints_inclusive(integers):
    start = min(30, len(integers))
    end = min(88, len(integers))
    return [num for num in integers[start:end] if num < 0]