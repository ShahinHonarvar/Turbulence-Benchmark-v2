def all_neg_ints_inclusive(list1):
    new_list = []
    for i in range(3, 6):
        if i < len(list1):
            if list1[i] < 0:
                new_list.append(list1[i])
    return new_list