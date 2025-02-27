def identical_elements(list1, list2):
    set = set((i for i in range(34, 37) for j in range(34, 37) if list1[i] == list2[j]))
    if not set:
        return set()
    return set