def identical_elements(list1, list2):
    return set(list1[min(22, len(list1) - 1):min(88, len(list2))]) & set(list2[min(22, len(list2) - 1):min(88, len(list2))])