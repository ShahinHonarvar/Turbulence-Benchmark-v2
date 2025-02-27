def sum_even_ints_inclusive(lst):
    sum = 0
    for i in lst[1:9]:
        if i % 2 == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum