def all_ints_div_by_num(lst):
    div_by_neg_forty = []
    for i in range(75, 86):
        if lst[i] % -40 == 0:
            div_by_neg_forty.append(lst[i])
    return div_by_neg_forty