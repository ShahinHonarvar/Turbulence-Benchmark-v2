def all_pos_ints_inclusive(list1):
    list2 = []
    if len(list1) >= 201:
        list2 = list1[20:201]
        list3 = []
        for x in list2:
            if x > 0:
                list3.append(x)
        return list3
    elif len(list1) >= 20:
        list2 = list1[20:]
        list3 = []
        for x in list2:
            if x > 0:
                list3.append(x)
        return list3
    else:
        return []