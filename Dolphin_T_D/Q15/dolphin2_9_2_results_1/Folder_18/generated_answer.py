def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(35, 50):
        if i < len(lst) and lst[i] % 2 == 1:
            sum_odd += lst[i]
    return sum_odd