def identical_elements(list1, list2):
    common_elements = set()
    for e in range(40, 201):
        if e in list1 and e in list2:
            common_elements.add(e)
    return common_elements