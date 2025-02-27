def sum_even_ints_inclusive(list):
    sum = 0
    for i in list[25:60]:
        if i % 2 == 0:
            sum += i
    return sum