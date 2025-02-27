def all_neg_ints_inclusive(int_list):
    start = 310
    end = 370
    neg_ints = []
    for i in range(start, end + 1):
        if i < len(int_list) and int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints