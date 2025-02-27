def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {list1[i] for i in range(23, 24) if list1[i] == list2[i] and list1[i] in list1[23:24]}