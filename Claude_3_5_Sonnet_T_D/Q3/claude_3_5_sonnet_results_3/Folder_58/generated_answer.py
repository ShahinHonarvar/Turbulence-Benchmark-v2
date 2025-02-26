def all_pos_ints_inclusive(integers):
    start_index = 209
    end_index = 557
    result = []
    if len(integers) <= start_index:
        return result
    for i in range(start_index, min(end_index, len(integers))):
        if integers[i] > 0:
            result.append(integers[i])
    return result