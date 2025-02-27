def identical_elements(list1, list2):
    if len(list1) == len(list2):
        return set(list1[50:201]) & set(list2[50:201])
    else:
        raise ValueError('Both lists must have the same size.')