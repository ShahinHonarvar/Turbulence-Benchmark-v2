def all_odd_ints_inclusive(ints):
    odds = []
    for i in range(max(6, 0), min(9, len(ints))):
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds