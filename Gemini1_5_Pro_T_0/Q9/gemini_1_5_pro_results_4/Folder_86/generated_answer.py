def all_odd_ints_inclusive(lst):
    odds = []
    for i in range(max(0, 31), min(len(lst), 35)):
        if lst[i] % 2 != 0:
            odds.append(lst[i])
    return odds