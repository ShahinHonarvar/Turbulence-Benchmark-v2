def identical_elements(list1, list2):
    index_range = range(68, 87)
    elements1 = {list1[i] for i in index_range if i < len(list1)}
    elements2 = {list2[i] for i in index_range if i < len(list2)}
    return elements1.intersection(elements2)