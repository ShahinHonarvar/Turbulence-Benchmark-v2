def all_ints_not_div_by_num(num_list):
    c = num_list[38:52]
    a = []
    for num in c:
        if num % -41 != 0:
            a.append(num)
    if len(a) != 0:
        return a
    else:
        return []