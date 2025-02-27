def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    for i in range(22, 89):
        if list1[i] in list2[i]:
            return {list1[i]}
    return set()