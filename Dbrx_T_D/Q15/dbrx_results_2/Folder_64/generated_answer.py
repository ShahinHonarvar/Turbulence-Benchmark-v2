def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in lst[0:5]:
        if i % 2 != 0:
            sum += i
    return sum