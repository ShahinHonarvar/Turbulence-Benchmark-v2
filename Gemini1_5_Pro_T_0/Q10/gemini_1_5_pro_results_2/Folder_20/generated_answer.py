def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(59, 93):
        if i < len(ints) and ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds