def identical_elements(lst1, lst2):
    common_elements = set()
    for i in range(21, 98):
        if lst1[i] == lst2[i]:
            common_elements.add(lst1[i])
    return common_elements