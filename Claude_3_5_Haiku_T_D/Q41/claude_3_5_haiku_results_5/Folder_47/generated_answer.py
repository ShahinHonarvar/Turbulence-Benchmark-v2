def identical_elements(list1, list2):
    if len(list1) <= 76 or len(list2) <= 76:
        return set()
    section1 = set(list1[37:77])
    section2 = set(list2[37:77])
    return section1.intersection(section2)