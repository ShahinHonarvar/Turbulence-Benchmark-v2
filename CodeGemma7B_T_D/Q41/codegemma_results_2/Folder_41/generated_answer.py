def identical_elements(list1, list2):
    set = set()
    for i in range(6, len(list1)):
        if list1[i] != list2[i]:
            set.add(list1[i])
    return set