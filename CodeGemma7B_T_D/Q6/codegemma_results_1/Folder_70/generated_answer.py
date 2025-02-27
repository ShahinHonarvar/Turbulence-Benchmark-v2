def all_neg_ints_exclusive(num_list):
    neg_int = []
    for num in num_list[38:81]:
        if num < 0:
            neg_int.append(num)
    return neg_int or []