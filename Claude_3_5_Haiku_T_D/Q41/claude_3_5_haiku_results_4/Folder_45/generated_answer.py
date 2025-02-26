def identical_elements(list1, list2):
    return set((x for i in range(30, 201) if (x := list1[i]) == list2[i]))