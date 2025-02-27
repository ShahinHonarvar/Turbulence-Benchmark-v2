def identical_elements(lst1, lst2):
    intersection = set()
    for i in range(43, 87):
        if lst1[i] == lst2[i]:
            intersection.add(lst1[i])
    return intersection