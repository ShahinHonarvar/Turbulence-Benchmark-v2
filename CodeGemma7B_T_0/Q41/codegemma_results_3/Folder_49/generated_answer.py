def identical_elements(list1, list2):
    return set([item for item in list1[80:201] for item in list2[80:201] if item in list1 and item in list2])