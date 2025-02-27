def identical_elements(list1, list2):
    elements = set()
    len1, len2 = (len(list1), len(list2))
    if len1 != len2:
        return elements
    for i in range(50, min(55, len1)):
        if list1[i] in list2:
            elements.add(list1[i])
    return elements