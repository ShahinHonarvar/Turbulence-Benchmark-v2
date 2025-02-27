def identical_elements(lst1, lst2):
    if len(lst1) != len(lst2) or len(lst1) < 58:
        return set()
    return set(lst1[56:58]) & set(lst2[56:58])