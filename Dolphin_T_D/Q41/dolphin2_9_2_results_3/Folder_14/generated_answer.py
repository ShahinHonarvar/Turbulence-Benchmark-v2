def identical_elements(list1, list2):
    set_elements = set()
    for i in range(5, 8):
        for ele in (list1, list2):
            if ele[i] == ele[i + 1]:
                set_elements.add(ele[i])
    return set_elements