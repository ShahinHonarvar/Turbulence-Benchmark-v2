def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(43, 87):
        if i >= len(ints):
            break
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds