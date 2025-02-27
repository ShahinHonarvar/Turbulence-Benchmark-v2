def identical_elements(list1, list2):
    return set((x for x in list1[12:92] for y in list2[12:92] if x == y))