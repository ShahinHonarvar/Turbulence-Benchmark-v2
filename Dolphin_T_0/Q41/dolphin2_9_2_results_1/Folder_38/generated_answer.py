def identical_elements(list1, list2):
    return set([element for index in range(22, 64) if element in list1[index:64] for element in list2[index:64] if element in list1[index:64]])