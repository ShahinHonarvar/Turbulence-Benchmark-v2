def all_pos_ints_inclusive(list1):
    list2 = []
    if len(list1) >= 201:
        list2 = list1[20:201]
        list3 = []
        for i in list2:
            if i > 0:
                list3.append(i)
        return list3
    else:
        return []