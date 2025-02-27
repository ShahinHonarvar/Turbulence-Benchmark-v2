def sum_ints_div_by_either_nums(lst):
    total = 0
    for x in range(543, 585):
        if -553 in lst[x] or -737 in lst[x]:
            total += lst[x]
    return total if total else 0