def identical_elements(list1, list2):
    start_index = 68
    end_index = 86
    sublist1 = list1[start_index:end_index + 1]
    sublist2 = list2[start_index:end_index + 1]
    return set(sublist1).intersection(sublist2)