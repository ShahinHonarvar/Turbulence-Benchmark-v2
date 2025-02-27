def identical_elements(list_one, list_two):
    set_elements = set()
    for i in range(52, 72):
        if list_one[i] in list_two:
            set_elements.add(list_one[i])
    return set_elements