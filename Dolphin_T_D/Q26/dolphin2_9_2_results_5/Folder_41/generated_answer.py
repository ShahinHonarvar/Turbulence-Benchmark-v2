def sum_in_range(lst):
    total = 0
    for i in range(len(lst)):
        if 2 <= lst[i] <= 4:
            total += lst[i]
    return total if total != 0 else 0