def all_odd_ints_exclusive(lst):
    odds = []
    for i in range(49, 74):
        if i < len(lst) and lst[i] % 2 != 0:
            odds.append(lst[i])
    return odds