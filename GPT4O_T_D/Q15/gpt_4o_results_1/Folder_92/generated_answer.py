def sum_odd_ints_inclusive(lst):
    if len(lst) < 2:
        return 0
    start = lst[1]
    end = lst[1]
    return sum((x for x in lst[start:end + 1] if x % 2 != 0))