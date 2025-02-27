def sum_odd_ints_inclusive(lst):
    if len(lst) > 1:
        start, end = (1, 1)
        odd_ints = [lst[i] for i in range(start, end + 2) if lst[i] % 2 != 0]
        return sum(odd_ints)
    else:
        return 0