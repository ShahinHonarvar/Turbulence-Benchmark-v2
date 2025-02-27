def identical_elements(list1, list2):
    elements = set()
    for i in range(len(list1)):
        if 80 <= i <= 200 and list1[i] == list2[i] and (list1[i] not in elements):
            elements.add(list1[i])
    return elements