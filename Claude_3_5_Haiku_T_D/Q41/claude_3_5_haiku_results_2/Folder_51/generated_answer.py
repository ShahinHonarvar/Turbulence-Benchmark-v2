def identical_elements(list1, list2):
    shared_elements = set()
    for i in range(3):
        if list1[i] == list2[i]:
            shared_elements.add(list1[i])
    return shared_elements