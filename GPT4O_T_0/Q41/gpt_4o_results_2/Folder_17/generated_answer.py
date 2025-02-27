def identical_elements(list1, list2):
    if len(list1) < 79 or len(list2) < 79:
        return set()
    return set(list1[62:79]).intersection(list2[62:79])