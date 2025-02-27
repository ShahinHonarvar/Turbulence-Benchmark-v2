def identical_elements(list1, list2):
    return set((e for i, e in enumerate(list1[70:85]) if e in list2[70:85]))