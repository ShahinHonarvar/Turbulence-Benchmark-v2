def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set((x for i, x in enumerate(list1) if i >= 50 and i <= 200 and (x in list2)))