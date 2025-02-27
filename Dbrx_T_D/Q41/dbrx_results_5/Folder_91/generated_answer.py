def identical_elements(list1, list2):
    elements = set()
    for i in range(min(len(list1), len(list2))):
        if list1[i] == list2[i]:
            elements.add(list1[i])
    return elements.intersection(list1[0:5], list2[0:5])