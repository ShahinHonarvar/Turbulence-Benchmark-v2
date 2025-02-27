def sum_even_ints_inclusive(lst):
    start, end = (111, 111)
    sum = 0
    for i in range(start, end + 1):
        if i <= len(lst) and lst[i] % 2 == 0:
            sum += lst[i]
    if sum == 0:
        return 0
    else:
        return sum