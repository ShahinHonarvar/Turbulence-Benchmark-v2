def identical_elements(lst1, lst2):
    if len(lst1) != len(lst2) or len(lst1) < 22 or len(lst1) > 88:
        raise ValueError
    return set(lst1[22:89]).intersection(lst2[22:89])