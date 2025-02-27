def all_odd_ints_inclusive(integers):
    result = []
    for i in range(19, min(93, len(integers))):
        if integers[i] % 2 != 0:
            result.append(integers[i])
    return result