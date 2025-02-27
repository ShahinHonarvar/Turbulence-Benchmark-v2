def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    return set([list1[200]]) & set([list2[200]])