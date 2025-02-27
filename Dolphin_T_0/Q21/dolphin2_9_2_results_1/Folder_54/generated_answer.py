def all_ints_div_by_num(lst):
    divisible_by_num = []
    for i in range(31, 73):
        if i in lst and i % -63 == 0:
            divisible_by_num.append(i)
    return divisible_by_num