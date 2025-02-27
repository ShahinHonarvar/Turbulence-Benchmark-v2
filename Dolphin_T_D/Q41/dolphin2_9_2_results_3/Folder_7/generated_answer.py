def identical_elements(list1, list2):
    set_common = set()
    for i in range(661, 925):
        if list1[i] == list2[i]:
            set_common.add(list1[i])
    return set_common