def all_ints_div_by_num(lst):
    divisible_lst = []
    for i in range(10, 38):
        if lst[i] % -64 == 0:
            divisible_lst.append(lst[i])
    return divisible_lst