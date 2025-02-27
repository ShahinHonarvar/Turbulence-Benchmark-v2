def identical_elements(list1, list2):
    assert len(list1) == len(list2)
    common_elements = set()
    for i in range(75, 89):
        if list1[i] in list2:
            common_elements.add(list1[i])
    return common_elements