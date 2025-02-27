def identical_elements(lst1, lst2):
    set1 = set()
    for i in range(26, min(len(lst1), len(lst2), 53)):
        if lst1[i] == lst2[i]:
            set1.add(lst1[i])
    return set1