def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(max(94, len(ints))):
        if i >= 93 and i < 94 and (ints[i] % 2 != 0):
            odds.append(ints[i])
    return odds