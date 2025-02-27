def all_odd_ints_inclusive(ints):
    odds = []
    for i in range(max(23, len(ints) - 1), 22, -1):
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds