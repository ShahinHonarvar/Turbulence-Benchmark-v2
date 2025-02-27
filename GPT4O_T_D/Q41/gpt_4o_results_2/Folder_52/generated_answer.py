def identical_elements(list1, list2):
    start = 28
    end = 39
    elements_list1 = set(list1[start:end])
    elements_list2 = set(list2[start:end])
    return elements_list1.intersection(elements_list2)