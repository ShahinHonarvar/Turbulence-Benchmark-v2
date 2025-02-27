def identical_elements(lst1, lst2):
    if len(lst1) != len(lst2):
        return set()
    return set(lst1[200:201]) & set(lst2[200:201])