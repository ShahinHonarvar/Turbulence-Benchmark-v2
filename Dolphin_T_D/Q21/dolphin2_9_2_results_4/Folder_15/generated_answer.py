def all_ints_div_by_num(lst):
    divisible = []
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            divisible.append(lst[i])
    return divisible