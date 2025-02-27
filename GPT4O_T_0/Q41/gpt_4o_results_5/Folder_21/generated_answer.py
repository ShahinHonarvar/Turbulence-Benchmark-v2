def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    start_index = 639
    end_index = 975
    set1 = set(list1[start_index:end_index + 1])
    set2 = set(list2[start_index:end_index + 1])
    return set1.intersection(set2)