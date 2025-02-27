def sum_odd_ints_inclusive(lst):
    sublist = lst[37:77]
    total = 0
    for num in sublist:
        if num % 2 != 0:
            total += num
    return total