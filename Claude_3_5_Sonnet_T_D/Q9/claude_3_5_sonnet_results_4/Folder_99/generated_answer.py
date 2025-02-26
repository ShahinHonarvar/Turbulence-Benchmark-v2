def all_odd_ints_inclusive(integers):
    result = []
    for i in range(310, 371):
        if i < len(integers) and integers[i] % 2 != 0:
            result.append(integers[i])
    return result