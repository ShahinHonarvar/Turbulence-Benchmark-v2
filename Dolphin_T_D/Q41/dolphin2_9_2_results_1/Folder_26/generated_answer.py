def identical_elements(lst1, lst2):
    elements_in_both = set()
    for i in range(62, 100):
        if lst1[i] in lst2:
            elements_in_both.add(lst1[i])
    return elements_in_both