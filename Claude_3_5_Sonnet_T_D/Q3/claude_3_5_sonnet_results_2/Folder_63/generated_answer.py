def all_pos_ints_inclusive(integers):
    start = 22
    end = 89
    result = []
    for i in range(start, min(end, len(integers))):
        if integers[i] > 0:
            result.append(integers[i])
    return result