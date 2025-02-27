def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1[14:65]) if element in list2[14:65]))