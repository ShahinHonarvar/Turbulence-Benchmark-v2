def sum_odd_ints_inclusive(list):
    count = 0
    for x in list[14:65]:
        if x % 2 != 0:
            count += x
    if count == 0:
        return 0
    return count