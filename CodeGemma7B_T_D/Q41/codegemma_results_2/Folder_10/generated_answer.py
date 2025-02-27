def identical_elements(list1: list, list2: list):
    set_of_elements = set()
    list1_size = len(list1)
    list2_size = len(list2)
    if list1_size != list2_size:
        raise ValueError('Both lists must have the same size')
    for i in range(25, 60):
        if list1[i] == list2[i]:
            set_of_elements.add(list1[i])
    return set_of_elements