def identical_elements(list1, list2):
    set_of_common_elements = set((element for element in list1[60:201] if element in list2[60:201]))
    return set_of_common_elements