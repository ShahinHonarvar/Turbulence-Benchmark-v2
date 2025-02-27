def sum_odd_ints_inclusive(lst):
    sum = 0
    range_lst = lst[56:58]
    for i in range_lst:
        if i % 2 != 0:
            sum += i
    return sum