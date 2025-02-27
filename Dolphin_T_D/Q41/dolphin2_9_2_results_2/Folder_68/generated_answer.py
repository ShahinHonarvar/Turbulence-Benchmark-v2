def identical_elements(list1, list2):
    return set([elem for i in range(8) if elem in list1[i] and elem in list2[i]])