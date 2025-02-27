def identical_elements(lst1, lst2):
    res = set()
    for i in range(667, 775):
        if lst1[i] in lst2[i]:
            res.add(lst1[i])
    return res