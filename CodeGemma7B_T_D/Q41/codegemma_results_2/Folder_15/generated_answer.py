def identical_elements(list1, list2):
    set_in_both = set()
    for i in range(len(list1)):
        if i >= 2 and i <= 7 and (list1[i] in list2[i]) and (list2[i] in list1[i]):
            set_in_both.add(list1[i])
    return set_in_both