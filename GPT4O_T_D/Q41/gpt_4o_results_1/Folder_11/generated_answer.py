def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    start = 37
    end = 51
    sublist1 = set(list1[start:end + 1])
    sublist2 = set(list2[start:end + 1])
    return sublist1 & sublist2