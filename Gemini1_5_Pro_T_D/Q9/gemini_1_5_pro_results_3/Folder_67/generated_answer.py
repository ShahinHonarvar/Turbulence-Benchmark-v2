def all_odd_ints_inclusive(ints):
    odds = []
    for i in range(22, 51):
        if i >= len(ints):
            break
        if ints[i] % 2 != 0:
            odds.append(ints[i])
    return odds