def all_odd_ints_inclusive(ints):
    odds = []
    for i in range(max(5, len(ints)), min(7, len(ints)) + 1):
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds