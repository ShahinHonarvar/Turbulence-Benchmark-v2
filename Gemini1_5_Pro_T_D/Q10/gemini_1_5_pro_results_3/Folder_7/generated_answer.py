def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(324, 972):
        if i in range(len(ints)):
            if ints[i] % 2 != 0:
                odds.append(ints[i])
    return odds