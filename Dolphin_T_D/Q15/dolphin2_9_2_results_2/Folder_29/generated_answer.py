def sum_odd_ints_inclusive(lst):
    total = 0
    for i in lst[59:98]:
        if i % 2 == 1:
            total += i
    return total