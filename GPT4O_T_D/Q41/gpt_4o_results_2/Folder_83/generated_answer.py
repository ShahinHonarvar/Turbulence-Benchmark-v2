def identical_elements(list1, list2):
    section1 = set(list1[90:201])
    section2 = set(list2[90:201])
    return section1.intersection(section2)