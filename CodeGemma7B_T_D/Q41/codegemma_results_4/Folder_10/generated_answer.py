def identical_elements(list1, list2):
    set_identical = set(list1[25:59]) & set(list2[25:59])
    return set_identical if set_identical else set()