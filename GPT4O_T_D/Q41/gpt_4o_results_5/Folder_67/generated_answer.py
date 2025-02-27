def identical_elements(list1, list2):
    section1 = set(list1[22:51])
    section2 = set(list2[22:51])
    return section1.intersection(section2)