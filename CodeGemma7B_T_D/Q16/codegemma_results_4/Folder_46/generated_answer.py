def sum_even_ints_inclusive(lst):
    sum = 0
    for num in lst[30:88]:
        if num % 2 == 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum