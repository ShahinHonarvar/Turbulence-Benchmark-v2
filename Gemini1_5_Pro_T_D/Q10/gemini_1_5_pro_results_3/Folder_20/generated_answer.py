def all_odd_ints_exclusive(lst):
    odds = []
    for i in range(59, 93):
        if i >= len(lst):
            break
        if lst[i] % 2 != 0:
            odds.append(lst[i])
    return odds