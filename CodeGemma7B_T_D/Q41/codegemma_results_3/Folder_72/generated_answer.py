def identical_elements(list1, list2):
    result = set((item for item in list1[29:52] for item in list2[29:52] if item == item))
    return result or set()