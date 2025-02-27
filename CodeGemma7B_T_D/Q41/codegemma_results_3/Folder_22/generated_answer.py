def identical_elements(lst1, lst2):
    unique_elements = set()
    for i in range(40, 201):
        if lst1[i] == lst2[i]:
            unique_elements.add(lst1[i])
    return unique_elements