def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 30 or len(list1) > 48:
        return set()
    return set(filter(list1[30:49].__contains__, list2[30:49]))