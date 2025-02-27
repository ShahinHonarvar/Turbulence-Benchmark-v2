def identical_elements(list1, list2):
    index_range = range(62, 64)
    elements_from_list1 = {list1[i] for i in index_range if i < len(list1)}
    elements_from_list2 = {list2[i] for i in index_range if i < len(list2)}
    return elements_from_list1.intersection(elements_from_list2)