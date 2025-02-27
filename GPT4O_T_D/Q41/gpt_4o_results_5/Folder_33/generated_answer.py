def identical_elements(list1, list2):
    start_index = 667
    end_index = 774
    sublist1 = set(list1[start_index:end_index + 1])
    sublist2 = set(list2[start_index:end_index + 1])
    return sublist1.intersection(sublist2)