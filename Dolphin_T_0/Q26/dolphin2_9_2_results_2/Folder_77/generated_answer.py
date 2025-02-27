def sum_in_range(lst):
    total = 0
    for i in lst:
        if 136 <= i <= 618:
            total += i
    return total if total else 0