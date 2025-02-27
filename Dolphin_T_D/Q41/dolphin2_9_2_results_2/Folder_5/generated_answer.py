def identical_elements(lst1, lst2):
    set1 = set()
    set2 = set()
    for i in range(8, 10):
        if i < len(lst1):
            set1.add(lst1[i])
        if i < len(lst2):
            set2.add(lst2[i])
    return set1.intersection(set2)