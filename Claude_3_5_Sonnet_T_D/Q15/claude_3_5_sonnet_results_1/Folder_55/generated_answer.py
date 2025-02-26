def sum_odd_ints_inclusive(integers):
    result = 0
    for i in range(min(11, len(integers))):
        if integers[i] % 2 != 0:
            result += integers[i]
    return result