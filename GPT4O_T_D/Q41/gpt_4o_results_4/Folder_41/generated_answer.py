def identical_elements(list1, list2):
    if len(list1) < 7 or len(list2) < 7:
        return set()
    return set([list1[6]]).intersection([list2[6]])