def all_even_ints_inclusive(integers):
    start_index = 56
    end_index = 99
    result = []
    if len(integers) <= start_index:
        return result
    for i in range(start_index, min(end_index, len(integers))):
        if integers[i] % 2 == 0:
            result.append(integers[i])
    return result