def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i, num in enumerate(int_list):
        if i >= 209 and i <= 556 and (num < 0):
            neg_ints.append(num)
    return neg_ints