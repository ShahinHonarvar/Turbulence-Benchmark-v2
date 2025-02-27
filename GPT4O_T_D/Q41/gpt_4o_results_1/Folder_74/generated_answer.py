def identical_elements(list1, list2):
    sublist1 = list1[17:79] if len(list1) >= 79 else list1[17:]
    sublist2 = list2[17:79] if len(list2) >= 79 else list2[17:]
    return set(sublist1).intersection(sublist2)