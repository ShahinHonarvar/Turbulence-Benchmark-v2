def identical_elements(list1, list2):
    result = set(list1[62:93]) & set(list2[62:93])
    return result if result else set()