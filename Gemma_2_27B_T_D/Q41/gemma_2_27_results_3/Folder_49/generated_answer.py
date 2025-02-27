def identical_elements(list1, list2):
    return set([elem for i, elem in enumerate(list1[80:201]) if elem in list2[80:201]])