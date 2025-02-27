def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(386, 999):
        if i % 2 != 0 and i < len(ints):
            odds.append(ints[i])
    return odds