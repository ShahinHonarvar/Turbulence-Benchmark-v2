def identical_elements(list1, list2):
    set_elements = set(list1[8:10] + list2[8:10]).intersection(list1[8:10] + list2[8:10])
    return set_elements