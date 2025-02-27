def identical_elements(lst1, lst2):
    set_identical_elements = set()
    for i in range(33, 37):
        if lst1[i] == lst2[i]:
            set_identical_elements.add(lst1[i])
    return set_identical_elements