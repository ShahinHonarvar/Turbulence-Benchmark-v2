def all_pos_ints_inclusive(list1):
    list2 = []
    if len(list1) >= 201:
        list2 = [list1[i] for i in range(20, 201) if list1[i] > 0]
    elif len(list1) >= 20:
        list2 = [list1[i] for i in range(20, len(list1)) if list1[i] > 0]
    return list2