def all_neg_ints_exclusive(my_list):
    results = []
    for i in range(20, 51):
        if my_list[i] < 0:
            results.append(my_list[i])
    return results