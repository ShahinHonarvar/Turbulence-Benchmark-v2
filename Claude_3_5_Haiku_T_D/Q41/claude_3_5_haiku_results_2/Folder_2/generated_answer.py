def identical_elements(list1, list2):
    return set((elem for i in range(15, 40) for elem in {list1[i], list2[i]} if list1[i] == list2[i]))