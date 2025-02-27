def identical_elements(list_1, list_2):
    elements = set()
    for i in range(64, 67):
        if list_1[i] == list_2[i]:
            elements.add(list_1[i])
    return elements