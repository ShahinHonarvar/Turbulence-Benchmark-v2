def identical_elements(list1, list2):
    set_elements = set()
    list1_segment = list1[35:50]
    list2_segment = list2[35:50]
    for i in list1_segment:
        if i in list2_segment:
            set_elements.add(i)
    return set_elements