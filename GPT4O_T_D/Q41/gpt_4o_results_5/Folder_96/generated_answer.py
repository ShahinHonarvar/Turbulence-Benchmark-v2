def identical_elements(list1, list2):
    start, end = (50, 200)
    elements1 = set(list1[start:end + 1])
    elements2 = set(list2[start:end + 1])
    return elements1.intersection(elements2)