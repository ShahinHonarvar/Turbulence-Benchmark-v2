def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set(list1[29:52]).intersection(set(list2[29:52]))