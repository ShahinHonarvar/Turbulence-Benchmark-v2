def identical_elements(list1, list2):
    result = set(list1[12:93]).intersection(list2[12:93])
    return result if result else set()