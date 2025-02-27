def identical_elements(lst1, lst2):
    if len(lst1) == len(lst2):
        return set(lst1[6:7]) & set(lst2[6:7])
    else:
        return set()