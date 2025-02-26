def all_even_ints_inclusive(integers):
    start = 60
    end = 201
    result = []
    if len(integers) <= start:
        return result
    for i in range(start, min(end, len(integers))):
        if integers[i] % 2 == 0:
            result.append(integers[i])
    return result