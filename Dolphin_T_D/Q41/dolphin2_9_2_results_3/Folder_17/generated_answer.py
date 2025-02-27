def identical_elements(list1, list2):
    return set(list(filter(None, map(list1.__contains__, list2))))