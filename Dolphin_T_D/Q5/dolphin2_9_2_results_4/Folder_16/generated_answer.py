def all_neg_ints_inclusive(int_list):
    negative_ints = []
    for num in int_list[32:37]:
        if num < 0:
            negative_ints.append(num)
    return negative_ints