def identical_elements(list_1, list_2):
    set_common = set()
    for i in range(3):
        if list_1[i] == list_2[i]:
            set_common.add(list_1[i])
    return set_common