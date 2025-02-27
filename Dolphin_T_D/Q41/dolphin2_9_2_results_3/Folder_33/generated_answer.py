def identical_elements(list_1, list_2):
    range_elements = []
    for i in range(667, 775):
        if list_1[i] == list_2[i]:
            range_elements.append(list_1[i])
    return set(range_elements)