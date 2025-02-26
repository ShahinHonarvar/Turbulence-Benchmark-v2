def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    section1 = set(list1[200:201])
    section2 = set(list2[200:201])
    return section1.intersection(section2)