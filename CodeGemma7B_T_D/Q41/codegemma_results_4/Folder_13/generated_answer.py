def identical_elements(list_1, list_2):
    similar_elements = set()
    for i in range(25, 88):
        if list_1[i] in list_2 and list_2[i] in list_1:
            similar_elements.add(list_1[i])
    if len(similar_elements) == 0:
        return set()
    else:
        return similar_elements