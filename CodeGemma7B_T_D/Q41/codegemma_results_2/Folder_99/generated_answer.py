def identical_elements(lst1, lst2):
    set_of_identical_elements = set()
    for i in range(310, 371):
        if lst1[i] in lst2 and lst2[i] in lst1:
            set_of_identical_elements.add(lst1[i])
    return set_of_identical_elements