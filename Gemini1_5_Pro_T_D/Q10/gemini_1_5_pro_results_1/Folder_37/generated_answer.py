def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(len(ints)):
        if i > 0 and i < 2 and (ints[i] % 2 != 0):
            odds.append(ints[i])
    return odds