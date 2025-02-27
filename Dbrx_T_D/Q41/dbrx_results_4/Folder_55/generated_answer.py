def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {list1[i] for i in range(9, len(list1)) if list1[i] in list2 and list2[i] in list1 and (list2[i] == list1[i])}