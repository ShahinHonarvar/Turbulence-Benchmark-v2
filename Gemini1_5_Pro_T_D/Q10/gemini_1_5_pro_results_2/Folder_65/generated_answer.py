def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(42, 87):
        if i < len(ints) and ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds