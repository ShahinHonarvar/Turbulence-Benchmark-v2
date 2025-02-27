def sum_odd_ints_inclusive(lst):
    total = 0
    for i in lst[5:8]:
        if i % 2 != 0:
            total += i
    return total if total != 0 else None