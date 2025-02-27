def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 751:
        return set()
    return set(list1[246:751]).intersection(list2[246:751])