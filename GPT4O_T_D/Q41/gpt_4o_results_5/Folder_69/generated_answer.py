def identical_elements(list1, list2):
    if len(list1) < 36 or len(list2) < 36:
        return set()
    section1 = set(list1[32:36])
    section2 = set(list2[32:36])
    return section1.intersection(section2)