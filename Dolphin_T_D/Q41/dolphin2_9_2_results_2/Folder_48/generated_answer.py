def identical_elements(list1, list2):
    elements = []
    for i in range(533, 606):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                elements.append(list1[i])
    return set(elements)