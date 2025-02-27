def all_neg_ints_exclusive(int_list):
    start = 60
    end = 200
    neg_ints = []
    for i in range(start, end):
        if i < 0:
            neg_ints.append(int_list[i])
    return neg_ints