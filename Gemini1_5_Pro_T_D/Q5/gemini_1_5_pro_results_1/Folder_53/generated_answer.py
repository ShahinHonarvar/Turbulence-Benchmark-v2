def all_neg_ints_inclusive(list_of_ints):
    neg_ints = []
    if len(list_of_ints) < 100:
        return neg_ints
    if len(list_of_ints) > 200:
        upper_bound = 201
    else:
        upper_bound = len(list_of_ints)
    for i in range(100, upper_bound):
        if list_of_ints[i] < 0:
            neg_ints.append(list_of_ints[i])
    return neg_ints