def identical_elements(list1, list2):
    return set(list1[min(56, len(list1) - 1):min(99, len(list1))] & list2[min(56, len(list2) - 1):min(99, len(list2))])