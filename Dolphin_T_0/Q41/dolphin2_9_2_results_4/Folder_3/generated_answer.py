def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set([i for i in list1[62:93] if i in list2[62:93]])