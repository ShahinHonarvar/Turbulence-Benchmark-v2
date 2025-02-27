def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 557:
        return set()
    return set(list1[209:557]).intersection(list2[209:557])