def all_neg_ints_inclusive(numbers_list):
    if len(numbers_list) < 200:
        return []
    neg_ints = []
    for i in range(20, 201):
        if numbers_list[i] < 0:
            neg_ints.append(numbers_list[i])
    return neg_ints