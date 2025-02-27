def sum_even_ints_inclusive(l):
    total = 0
    for num in l[75:95]:
        if num % 2 == 0:
            total += num
    return total