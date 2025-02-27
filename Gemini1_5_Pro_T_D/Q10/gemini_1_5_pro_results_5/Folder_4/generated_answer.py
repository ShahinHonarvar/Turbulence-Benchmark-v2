def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(max(10, 0), min(len(ints), 76)):
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds