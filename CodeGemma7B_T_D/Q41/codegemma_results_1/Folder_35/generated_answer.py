def identical_elements(list1, list2):
    result = {item for item in list1[30:49] if item in list2[30:49]}
    return result or {}