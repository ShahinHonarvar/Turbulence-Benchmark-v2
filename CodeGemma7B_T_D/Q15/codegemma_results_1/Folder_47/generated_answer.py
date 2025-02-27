def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in lst[37:77]:
        if i % 2 != 0:
            sum += i
    return sum if sum != 0 else 0