def identical_elements(list1, list2):
    return set([elem for elem in set(list1[10:67]) if elem in set(list2[10:67])])