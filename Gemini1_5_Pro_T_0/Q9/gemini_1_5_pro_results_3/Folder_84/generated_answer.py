def all_odd_ints_inclusive(ints):
    odds = []
    for i in range(max(0, min(len(ints) - 1, 43)), min(len(ints), 87)):
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds