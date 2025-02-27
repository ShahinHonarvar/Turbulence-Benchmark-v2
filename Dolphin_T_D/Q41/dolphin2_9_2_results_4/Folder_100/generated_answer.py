def identical_elements(list1, list2):
    return set(filter(lambda x: x in list1[42:69] and x in list2[42:69], list1[42:69]))