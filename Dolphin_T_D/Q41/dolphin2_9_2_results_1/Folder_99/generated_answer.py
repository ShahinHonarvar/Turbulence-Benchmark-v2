def identical_elements(list1, list2):
    set1 = set()
    set2 = set()
    for i in range(310, 371):
        if i < len(list1) and i < len(list2):
            if list1[i] in set1:
                set1.remove(list1[i])
            else:
                set1.add(list1[i])
            if list2[i] in set2:
                set2.remove(list2[i])
            else:
                set2.add(list2[i])
    return set1.intersection(set2)