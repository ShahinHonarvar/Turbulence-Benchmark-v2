def sum_even_ints_inclusive(ls):
    sum_even_nums = 0
    for i in range(686, 988):
        if i < len(ls) and i >= 0 and (ls[i] % 2 == 0):
            sum_even_nums += ls[i]
    return sum_even_nums