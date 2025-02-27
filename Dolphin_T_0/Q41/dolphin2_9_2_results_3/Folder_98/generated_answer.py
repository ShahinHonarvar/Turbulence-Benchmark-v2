def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        return set()
    else:
        return set((i for i in list_1[0:6] if i in list_2[0:6]))