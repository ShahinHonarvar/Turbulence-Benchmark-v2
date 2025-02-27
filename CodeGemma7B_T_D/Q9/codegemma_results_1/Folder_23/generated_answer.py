def all_odd_ints_inclusive(lst):
    odds = []
    for i in lst[52:72]:
        if i % 2 != 0:
            odds.append(i)
    return odds