def identical_elements(list_1, list_2):
    set_ = set()
    for i in range(22, 51):
        if list_1[i] in list_2[i]:
            set_.add(list_1[i])
    return set_