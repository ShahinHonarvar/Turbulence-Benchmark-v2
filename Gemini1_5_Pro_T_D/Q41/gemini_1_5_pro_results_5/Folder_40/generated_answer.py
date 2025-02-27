def identical_elements(list1, list2):
    set1 = set()
    for element in list1[:2]:
        if element in list2[:2]:
            set1.add(element)
    return set1