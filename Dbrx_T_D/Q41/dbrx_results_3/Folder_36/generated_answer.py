def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set(list1[246:751]) & set(list2[246:751])