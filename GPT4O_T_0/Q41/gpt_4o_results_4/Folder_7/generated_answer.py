def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 925:
        return set()
    return set(list1[661:925]).intersection(list2[661:925])