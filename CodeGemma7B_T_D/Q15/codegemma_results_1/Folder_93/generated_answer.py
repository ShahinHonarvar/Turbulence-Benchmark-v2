def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for num in lst[75:95]:
        if num % 2 != 0:
            sum_odd += num
    if sum_odd == 0:
        return 0
    else:
        return sum_odd