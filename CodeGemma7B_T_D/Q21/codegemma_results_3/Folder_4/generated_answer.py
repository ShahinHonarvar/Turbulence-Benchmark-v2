def all_ints_div_by_num(l):
    temp = []
    for i in range(12, 93):
        if l[i] % -14 == 0:
            temp.append(l[i])
    return temp