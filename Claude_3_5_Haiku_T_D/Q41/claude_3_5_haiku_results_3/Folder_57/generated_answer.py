def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1) if 27 <= i <= 55 and element in list2[27:56] and (element in list1[27:56])))