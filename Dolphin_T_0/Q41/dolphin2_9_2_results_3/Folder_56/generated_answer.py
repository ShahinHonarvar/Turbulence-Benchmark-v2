def identical_elements(list1: list, list2: list) -> set:
    return set((i for i in list1[1:9] if i in list2[1:9]))