def identical_elements(list_one, list_two):
    unique_elements = set()
    for i in range(55, 99):
        if list_one[i] in list_two[i]:
            unique_elements.add(list_one[i])
    return unique_elements