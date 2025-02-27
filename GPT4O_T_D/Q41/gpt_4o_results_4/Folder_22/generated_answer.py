def identical_elements(list1, list2):
    sublist1 = list1[40:201]
    sublist2 = list2[40:201]
    return set(sublist1).intersection(sublist2)