def all_ints_div_by_num(lst):
    divisible_by_8 = []
    for i in range(0, 1):
        if i in lst and i % 8 == 0:
            divisible_by_8.append(i)
    return divisible_by_8