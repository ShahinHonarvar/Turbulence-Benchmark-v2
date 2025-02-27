def identical_elements(list1, list2):
    return set((element for i, element in enumerate(list1) if 59 <= i <= 97 and element in list2[59:98]))