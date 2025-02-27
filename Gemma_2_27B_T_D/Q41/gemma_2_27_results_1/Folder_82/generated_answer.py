def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[20:201]) if element in list2[20:201]))