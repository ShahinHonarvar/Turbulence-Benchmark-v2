def sum_in_range(list_integers):
    total = 0
    for i in list_integers:
        if i >= 39 and i <= 43:
            total += i
    return total if total != 0 else 0