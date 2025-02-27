def identical_elements(list1, list2):
    range_elements1 = [list1[i] for i in range(527, 539)]
    range_elements2 = [list2[i] for i in range(527, 539)]
    return set(filter(lambda x: x in range_elements1, range_elements2))