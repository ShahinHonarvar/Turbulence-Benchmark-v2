def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in lst[4:len(lst) + 1]:
        if i % 2 != 0:
            sum += i
    return sum