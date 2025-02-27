def identical_elements(list1, list2):
    set_identical = set()
    for i in range(10, 101):
        if list1[i] in list2[i]:
            set_identical.add(list1[i])
    return set_identical