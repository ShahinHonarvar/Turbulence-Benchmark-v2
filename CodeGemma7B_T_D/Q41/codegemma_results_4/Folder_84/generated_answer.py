def identical_elements(lst1, lst2):
    identical_elements = set()
    for i in range(43, 87):
        if lst1[i] == lst2[i]:
            identical_elements.add(lst1[i])
    return identical_elements