def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 976:
        return set()
    sublist1 = list1[639:976]
    sublist2 = list2[639:976]
    return set(sublist1).intersection(sublist2)