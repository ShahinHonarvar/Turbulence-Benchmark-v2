def identical_elements(lst1, lst2):
    set1 = set()
    for i in range(30, 201):
        if i < len(lst1) and i < len(lst2):
            set1.add(lst1[i])
            set1.add(lst2[i])
    return set1