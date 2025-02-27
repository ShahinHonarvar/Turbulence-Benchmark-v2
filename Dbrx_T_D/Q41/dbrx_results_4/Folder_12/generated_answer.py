def identical_elements(list1, list2):
    return set((i for i in set(list1[14:65]) & set(list2[14:65]) if list1.count(i) > 0 and list2.count(i) > 0))