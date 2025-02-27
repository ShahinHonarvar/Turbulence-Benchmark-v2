def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 751:
        return set()
    set1 = set(list1[246:751])
    set2 = set(list2[246:751])
    return set1 & set2