def identical_elements(list1, list2):
    shared_elements = []
    for i in range(262, 747):
        if list1[i] in list2:
            shared_elements.append(list1[i])
    return set(shared_elements)