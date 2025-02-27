def identical_elements(list1, list2):
    return set([item for item in list1 if item in list2 and list1.index(item) in range(0, 8)])