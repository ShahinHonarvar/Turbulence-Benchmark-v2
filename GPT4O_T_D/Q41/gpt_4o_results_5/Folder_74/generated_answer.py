def identical_elements(list1, list2):
    if not (17 <= len(list1) and 17 <= len(list2)):
        return set()
    subset1 = list1[17:79]
    subset2 = list2[17:79]
    return set(subset1).intersection(subset2)