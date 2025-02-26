def all_even_ints_inclusive(integers):
    result = []
    for i in range(min(11, len(integers))):
        if integers[i] % 2 == 0:
            result.append(integers[i])
    return result