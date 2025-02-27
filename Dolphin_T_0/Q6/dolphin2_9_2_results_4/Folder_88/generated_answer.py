def all_neg_ints_exclusive(listed_integers):
    list = []
    for neg_int in listed_integers[3:9]:
        if neg_int < 0:
            list.append(neg_int)
    return list